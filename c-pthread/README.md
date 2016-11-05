# [C] pthreadでスレッドプログラミング

## 簡単な例

pthreadで以下の挙動を満たす単純なスレッドを生成します。

- メインスレッドと子スレッド1個ずつだけ
- 子スレッドは1秒ずつ"."を標準出力に出力
- 子スレッドは10秒間実行したのち処理を終了する

```
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

void *func(){
     for (int ii = 0; ii < 10; ii++ ) {
          fprintf(stdout, ".");
          fflush(stdout);
          sleep(1);
     }
     fprintf(stdout, "\n");
     return NULL;
}


int main(int argc, char *argv[]) {
     int rc = 0;
     pthread_t child;
     rc = pthread_create(&child, NULL, &func, NULL);
     fprintf(stdout, "pthread_create returned %d\n", rc);

     rc = pthread_join(child, NULL);
     fprintf(stdout, "pthread_join returned %d\n", rc);
     return 0;
}
```

simple_thread.cをコンパイルして、simple_thread.outを生成します。

```
$ gcc simple_thread.c -o simple_thread.out

```

simple_thread.outを実行します。

```
$ time ./simple_thread.out
pthread_create returned 0
...........
pthread_join returned 0
./simple_thread.out  0.00s user 0.00s system 0% cpu 11.039 total
$
```

プログラムは10秒間、1秒ずつ"."を標準出力に出力したのち終了します。

## 子スレッドに引数を渡す

子スレッドに引数を渡して実行します。
スレッドの関数の引数はvoid型のポインタなので、呼び出し時にアドレスを渡しスレッド内でポインタのキャストを行います。
以下の例ではFunctionArgumentという構造体を定義しfunction_argument_tという型名で宣言して、
それを子スレッドとの値のやりとりに利用しています。

```
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

typedef struct FunctionArgument {
     int count;
     char *message;
} function_argument_t;

void *func(void *p){
     function_argument_t *func_arg = (function_argument_t *)p;
     for (int ii = 0; ii < func_arg->count; ii++ ) {
          fprintf(stdout, ".");
          fflush(stdout);
          sleep(1);
     }
     fprintf(stdout, "%s\n", func_arg->message);
     return NULL;
}


int main(int argc, char *argv[]) {
     int rc = 0;
     pthread_t child;
     function_argument_t func_arg = {10, "OK!!\n"};

     rc = pthread_create(&child, NULL, &func, &func_arg);
     fprintf(stdout, "pthread_create returned %d\n", rc);

     rc = pthread_join(child, NULL);
     fprintf(stdout, "pthread_join returned %d\n", rc);
     return 0;
}
```

## 子スレッドの戻り値を

子スレッドから返された値を取得します。

main関数で`void *child_rc_p`変数を追加しています。これは子スレッドが返却したアドレスを保持するためのポインタ変数です。`rc = pthread_join(child, &child_rc_p);` で第二引数にそのアドレスを渡します。pthread_join()の第二引数の型は`void **`です。

子スレッド内ではmalloc()で領域を確保し値を格納してそのポインタをreturnしています。
このreturnしたポインタがptread_join()の第二引数で渡したポインタにセットされます。

```
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>


void *func(){
     void *rc_p;
     rc_p = malloc(sizeof(int));
     if (rc_p == NULL) {
          fprintf(stderr, "Cannot allocate memory");
          return NULL;
     }
     for (int ii = 0; ii < 10; ii++ ) {
          fprintf(stdout, ".");
          fflush(stdout);
          sleep(1);
     }

     fprintf(stdout, "\n");

     *(int *)rc_p = 3;
     return rc_p;
}


int main(int argc, char *argv[]) {
     int rc = 0;
     void *child_rc_p;
     pthread_t child;

     rc = pthread_create(&child, NULL, &func, NULL);
     fprintf(stdout, "pthread_create returned %d\n", rc);

     rc = pthread_join(child, &child_rc_p);
     fprintf(stdout, "pthread_join returned %d\n", *(int *)child_rc_p);
     free(child_rc_p);
     return 0;
}
```
