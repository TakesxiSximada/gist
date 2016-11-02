int main(){
    const int real = 4;
    int *pointer = &real;
    *pointer = 9;
    return real;
}
