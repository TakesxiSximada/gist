int main(){
    int real = 0;
    int *pointer = &real;
    *pointer = 9;
    return real;
}
