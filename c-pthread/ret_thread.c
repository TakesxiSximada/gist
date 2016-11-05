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
