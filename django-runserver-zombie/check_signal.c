#include <stdio.h>
#include <signal.h>
#include <unistd.h>


void handler(int sig) {
     fprintf(stdout, "SIGNAL: %d\n", sig);
}


int main(int argc, char *argv[]) {
     signal(SIGTERM, handler);
     signal(SIGTERM, handler);
     signal(SIGINT, handler);
     signal(SIGHUP, handler);
     sleep(1000000);
     return 0;
}
