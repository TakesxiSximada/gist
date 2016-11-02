typedef struct {
     char *name;
     int age;
} user_t;

int main(){
     user_t user = {
          "Test",
          3
     };
     return user.age;
}
