# [C] シグナル処理

## signal() - シグナルハンドラを登録する

```
#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

void handle_signal(int sig) {
     printf("OK\n");
}

int main(int argc, char *argv[]) {
     if (SIG_ERR == signal(SIGHUP, handle_signal)) {
          fprintf(stderr, "Cannot set singal handler.");
     }
     sleep(100);
}
```

## raise() - 自分自身にシグナルを送信する

signal.h

## kill() - 他のプロセスにシグナルを送信する

```
#include <signal.h>
#include <stdio.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
     if (kill(12109, SIGHUP) != 0){
          fprintf(stderr, "error\n");
     }
     return 0;
}
```
