int main(){
    const int real = 4;
    const int *pointer = &real;
    *pointer = 9;
    return real;
}
