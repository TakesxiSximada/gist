# Cのconst宣言の有無で出力されるアセンブリに違いはあるか?


## constあり

const.c:

```
int main() {
     const int n = 0;
     return 0;
}
```

## constなし

noconst.c:

```
int main() {
     int n = 0;
     return 0;
}
```

## constの付け方

constは型宣言の前でも後でもつけられます。

```
const int n = 0;
```

もしくは

```
int const n = 0;
```

で、変数nがconst扱いになります。

## 比較

```
$ gcc -S const.c noconst.c
$ diff const.s noconst.s
$
```

差分はない。


## アセンブリコードを眺める

```
	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 10
	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp0:
	.cfi_def_cfa_offset 16
Ltmp1:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp2:
	.cfi_def_cfa_register %rbp
	xorl	%eax, %eax
	movl	$0, -4(%rbp)
	movl	$0, -8(%rbp)
	popq	%rbp
	retq
	.cfi_endproc


.subsections_via_symbols
```

## const宣言した変数を書き換えてみる

const_error.c:

```
int main() {
     const int n = 0;
     n = 1;
     return 0;
}
```

コンパイルします。

```
$ gcc -S const_error.c
const_error.c:3:8: error: read-only variable is not assignable
     n = 1;
     ~ ^
1 error generated.
```

コンパイルエラーしました。const宣言はコンパイラに影響する指示で、コンパイル時に領域への代入が行われないことをチェックします。

## const宣言ありのポインタの挙動

### const全くなし

pointer.c:

```
int main(){
    int real = 0;
    int *pointer = &real;
    *pointer = 9;
    return real;
}
```

realは実値、pointerはrealのアドレスを保持したポインタです。constは付いてません。
`*pointer = 9;` の行によりrealの値を1に変更しています。
このコードはコンパイルでき、標準出力にはrealの値が表示されます。

```
$ gcc pointer.c
$ ./a.out
9
$
```

### 実値にconst

今度はrealにconst宣言します。

pointer_const_real.c:

```
int main(){
    const int real = 0;
    int *pointer = &real;
    *pointer = 9;
    return real;
}
```

realはconst指定をしていますが、pointerにはconst指定をしていません。
コンパイルしてみるとこのコードはワーニングが出力されますが、コンパイルエラーにはなりません。

```
$ gcc pointer_const_real.c
pointer_const_real.c:5:10: warning: initializing 'int *' with an expression of type 'const int *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
    int *pointer = &real;
         ^         ~~~~~
1 warning generated.

```

出力されるワーニングは `warning: initializing 'int *' with an expression of type 'const int *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]` です。

実行すると0が出力されます｡
```
$ ./a.out
0
$
```

`*pointer = 9;` はどうなってしまったのでしょうか。

アセンブリコードを出力し確認します。

```
$ gcc -O0 -S pointer_const_real.s
```

pointer_const_real.s:

```
	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 10
	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp0:
	.cfi_def_cfa_offset 16
Ltmp1:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp2:
	.cfi_def_cfa_register %rbp
	xorl	%eax, %eax
	leaq	-8(%rbp), %rcx
	movl	$0, -4(%rbp)
	movl	$0, -8(%rbp)
	movq	%rcx, -16(%rbp)
	movq	-16(%rbp), %rcx
	movl	$9, (%rcx)
	popq	%rbp
	retq
	.cfi_endproc


.subsections_via_symbols
```
`movl	$0, -8(%rbp)` が `const int real = 4;` です。
変数は次のように展開されています。

- real: `-8(%rbp)`
- pointer: `-16(%rbp)`

realのアドレスを計算して、%rcxに保持しています。
この時点で%rcxにはrealのアドレスが格納されています。

```
    leaq	-8(%rbp), %rcx
```

%rcxにはrealのアドレスが入っています。ここでpointerにrealのアドレスを格納しています。

```
	movq	%rcx, -16(%rbp)
	movq	-16(%rbp), %rcx
```

rcxにはrealのアドレスが入っていましt。ここでrealの値を上書きしています。

```
	movl	$9, (%rcx)
```

そして`-16(%rbp)` はpointerの領域です。今realの値は9です。しかし、`return real;` が行われた形跡がありません。
%raxに戻り値の値が設定されるべきなので、期待としては`movq -8(%rbp), %rax`が出力されていることですが、そのコードはありません。

試しに以下を追加してコンパイルすると、9が返されるようになります。

```
	movl	$9, (%rcx)
    movq	-8(%rbp), %rax  ## <- ここを追加
	popq	%rbp
```

他のWebの記事を見ると今回の結果と異なる内容のものをちらほら見かけます。
コンパイラによってこの挙動は違うかもしれません。
今回仕様しているコンパイラは以下です。

```
$ gcc -v
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 7.0.0 (clang-700.0.72)
Target: x86_64-apple-darwin14.5.0
Thread model: posix
```

### ポインタにconst

今度はrealのポインタであるpointerにconst宣言します。

```
int main(){
    int real = 4;
    const int *pointer = &real;
    *pointer = 9;
    return real;
}
```

これはコンパイルするとコンパイルエラーになります。

```
$ gcc  pointer_const_pointer.c
pointer_const_pointer.c:4:14: error: read-only variable is not assignable
    *pointer = 9;
    ~~~~~~~~ ^
1 error generated.
$
```

const宣言したポインタから参照した領域を変更はできないようです。
ただしreal自体はconst宣言していないので、ポインタ経由でななくrealを直々に変更は可能です。


```
int main(){
    int real = 4;
    const int *pointer = &real;
    real = 9;  # <- これはできる
    return real;
}
```


### 実値とポインタにconst

realとrealのポインタであるpointerの両方にconst宣言します。

```
int main(){
    const int real = 4;
    const int *pointer = &real;
    *pointer = 9;
    return real;
}
```

これは`*pointer = 9;`でconst宣言した変数を変更しようとしているので当然コンパイルエラーです。

```
$ gcc pointer_const_real_and_pointer.c
pointer_const_real_and_pointer.c:4:14: error: read-only variable is not assignable
    *pointer = 9;
    ~~~~~~~~ ^
1 error generated.
```

### ポインタマークの後にconst

`const int n = 0;` も `int const n = 0;` も同じであることは説明しました。
では `int * const p;` はどのような扱いになるのでしょうか。


```
int main(){
    int real = 0;
    int * const pointer = &real;
    *pointer = 9;
    return real;
}
```

このコードはコンパイルできます。実行も意図通りになります。

```
$ gcc pointer_const_after_star.c
$ ./a.out
$ echo $?
9
```

参照先は変更できるようです。

ではpointerに格納されているアドレスは書き換え可能でしょうか?

```
int main(){
    int real = 0;
    int other = 1;
    int * const pointer = &real;
    pointer = &other;
    *pointer = 9;
    return real;
}
```

ここではotherという別の変数を用意して`pointer = &other;`でアドレスを変更しようとしています。
これはコンパイルエラーになります。

```
$ gcc  pointer_const_after_star_change_address.c
pointer_const_after_star_change_address.c:5:13: error: read-only variable is not assignable
    pointer = &other;
    ~~~~~~~ ^
1 error generated.
$
```

## まとめ

- constは変数の変更を禁止するコンパイラへの命令
- 変数宣言の型名の前後どちらでも指定が可能
- constを指定した変数のアドレスを持つポインタがあった場合、変数の値変更をしてもエラーにはならないがワーニングが出る
  - コンパイラによって挙動がちがうかもしれない
  - この状態での挙動は意図しない状態になる
- ポインタに対するconst指定はconstの位置のよって挙動が変わる
  - 型の前の場合はポインタが指し示す変数の値変更禁止
  - 型の後ろでポインタマークの前の場合はポインタが指し示す変数の値変更禁止
  - ポインタマークの後ろの場合はポインタが保持するアドレスの書き換え禁止
