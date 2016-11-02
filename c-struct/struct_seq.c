struct User {
     char *name;
     int age;
};

int main(){
     struct User user = {"Test", 2};
     struct User *pointer = &user;
     return pointer->age;
}
