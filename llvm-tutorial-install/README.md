# LLVMでLLVM-IRを生成して眺める

## LLVM

コンパイラのフレームワーク。あらゆるステージで最適化するように設計されている。
なんとなく行っている意味はわかるけど具体的にどこがどうかはあんまりピンとこない。
仮装マシン上で動作する中間言語(LLVM-IR)を生成して、そこから動作マシーンに対応するプログラムを生成するっぽい。

`LLVM とは、コンパイル時、リンク時、実行時などあらゆる時点でプログラムを最適化するよう設計された、任意のプログラミング言語に対応可能なコンパイラ基盤である。`
Wikipediaよりhttps://ja.wikipedia.org/wiki/LLVM

## Clang / Clang++

LLVMコンパイラフロントエンド。C, C++, Objective-C, Objective-C++に対応している。

## LLVM-IR

LLVMで使われる中間言語。
例えばClangでC言語のファイルをコンパイル/リンクすると
LLVM-IRが生成され最適化されたのち、実行可能なバイナリファイルが生成される。

## CのソースをLLM-IRに変換する

単純なHello worldのCのコードをLLVM-IRに変換してみる。

main.c:

```
#include <stdio.h>

int main(int argc, char *argv[]) {
     printf("Hello world!!\n");
     return 2;
}
```

このファイルをclangコマンドでIIVM-IRにする。

```
$ clang -S -emit-llvm main.c
```

実行すると `main.ll` が生成される。

main.ll:

```
; ModuleID = 'main.c'
target datalayout = "e-m:o-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx10.10.0"

@.str = private unnamed_addr constant [15 x i8] c"Hello world!!\0A\00", align 1

; Function Attrs: nounwind ssp uwtable
define i32 @main(i32 %argc, i8** %argv) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i8**, align 8
  store i32 0, i32* %1
  store i32 %argc, i32* %2, align 4
  store i8** %argv, i8*** %3, align 8
  %4 = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([15 x i8]* @.str, i32 0, i32 0))
  ret i32 2
}

declare i32 @printf(i8*, ...) #1

attributes #0 = { nounwind ssp uwtable "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="core2" "target-features"="+ssse3,+cx16,+sse,+sse2,+sse3" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="core2" "target-features"="+ssse3,+cx16,+sse,+sse2,+sse3" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"PIC Level", i32 2}
!1 = !{!"Apple LLVM version 7.0.0 (clang-700.0.72)"}
```

## LLVM-IRの解説

LLVM-IRは言語ドキュメントがあるのでそちらをみるとよい。
http://www.h3.dion.ne.jp/~mu-ra/llvm/LangRefJ.html

以下では少しだけ解説していく。

### define - 関数定義

`define` キーワードを使って関数を定義できます。
ここではmain()関数を定義しています。

```
define i32 @main(i32 %argc, i8** %argv) #0 {
  ; ....
  ret i32 2
}

```

`define` の直後にはその関数が返すべき値の型を指定します。関数名の頭には `@` を必ずつけます。
その後ろの `()` 内に引数を定義します。関数のブロックは `{}` で囲みます。

### 戻り値

関数が返す値をretで指定できます。`ret 型 値` です。

```
  ret i32 2
```

型は関数宣言時の型と一致しなければなりません。
試しにmain()関数の戻り値型をvoidに指定してみます。

```
define void @main(i32 %argc, i8** %argv) #0 {
```

clangコマンドで編集したmain.llをコンパイルすると次のようにコンパイルエラーになります。

```
$ clang main.ll
main.ll:16:7: error: value doesn't match function result type 'void'
  ret i32 2
      ^
1 error generated.
```

### = - 代入

`=` を使うと右辺の値を左辺の領域に代入できます。

### レジスタ

`%1` や `%2` などはレジスタです。レジスタには値を保持できます。
レジスタは必ず `%` から始まります。


### alloca - スタックメモリ割当

スタックフレームのメモリを割り当てて、ポインタを返します。

```
%1 = alloca i32, align 4
```

alignは指定したバイト数でアラインメントします｡
領域が確保できない時の挙動は未定義です。

### store - メモリへの書き出し

`store` を使ってメモリ領域へ値を書き込みます。

次の例ではi32型の0という値を、
%1に保存されているi32型のポインタの先のメモリアドレスに保存します。

```
  store i32 0, i32* %1
```

### call - 関数呼び出し

`call` を使って関数を呼び出せます。


```
  %4 = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([15 x i8]* @.str, i32 0, i32 0))
```

### コメント

行の `;` 以降がコメントになります。
