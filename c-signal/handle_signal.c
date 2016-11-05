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
