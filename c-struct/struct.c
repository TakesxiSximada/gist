struct User {
     char *name;
     int age;
};

int main(){
     struct User user = {
          "Test",
          3
     };
     return user.age;
}
