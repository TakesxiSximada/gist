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
