int main(){
    int real = 0;
    int * const pointer = &real;
    *pointer = 9;
    return real;
}
