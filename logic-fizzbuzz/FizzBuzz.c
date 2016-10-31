#include <stdio.h>

int main(int argc, char *argv[]){
     for(int ii = 0; ii <= 100; ii++){
          if (ii % 15 == 0){
               printf("FizzBuzz\n");
          } else if (ii % 3 == 0) {
               printf("Fizz\n");
          } else if (ii % 5 == 0) {
               printf("Buzz\n");
          } else {
               printf("%d\n", ii);
          }
     };
     return 0;
}
