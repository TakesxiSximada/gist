#include <stdio.h>

int main() {
     int no_const_value = 0;
     int *const_value_p = &no_const_value;
     *const_value_p = 1;
     printf("%d\n", *const_value_p);
     return 0;
}
