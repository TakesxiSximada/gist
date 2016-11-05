#include <signal.h>
#include <stdio.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
     if (kill(12109, SIGHUP) != 0){
          fprintf(stderr, "error\n");
     }
     return 0;
}
