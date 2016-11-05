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
