#include <iostream>

using namespace std;

int main(int argc, char** argv){
     for(int ii = 0; ii <= 100; ii++){
          if (ii % 3 == 0 && ii % 5 == 0){
               cout << "FizzBuzz\n";
          } else if (ii % 3 == 0) {
               cout << "Fizz\n";
          } else if (ii % 5 == 0) {
               cout << "Buzz\n";
          } else {
               cout << ii << "\n";
          }
     };
     return 0;
}
