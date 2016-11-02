int main(){
    int real = 0;
    int other = 1;
    int * const pointer = &real;
    pointer = &other;
    *pointer = 9;
    return real;
}
