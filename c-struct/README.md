# 構造体

## 定義

```
struct User {
     char *name;
     int age;
};
```

## 使い方

```
int main(){
     struct User user = {
          "Test",
          3
     };
     return user.age;
}
```
## 配列での初期化

```
     struct User users[3] = {
          {"Test", 3},
          {"Test1", 4},
          {"Test2", 6}
     };

```

## アロー演算子

構造体のポインタから実態の属性を指し示す時に使う。

```
     struct User user = {"Test", 2};
     struct User *pointer = &user;
     return pointer->age;

```

## typedef struct

構造体を型宣言する方法です。typedefで定義すると、宣言時にstructを書く必要がなくなります。
ただし、構造体の情報が見えにくくなるのでtypedefが嫌われることもあります。


### 形式1

```
typedef struct User {
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

```
### 形式1

```
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

```
