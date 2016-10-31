# FizzBuzz言語別実装

しばしばFizzBuzzをホワイトボードに書かせるという
エンジニアの技量を測るのに最も適したソリューションを取りいている方々がおられます。
きっとFizzBuzzさえかければ、そのシステムは開発できるほどシンプルなんですね。
とても素晴らしいのでみなさんもそれに習ってFizzBuzzをホワイトボードに積極的に書かせましょう!!

## FizzBuzzとは

1. 1から大きい方に順番に標準出力に1行ずつ表示していく
2. ただしその数が3の倍数のときはfizzと表示する
3. ただしその数が5の倍数のときはbuzzと表示する
4. ただしその数が3と5の倍数のときはfizzbuzzと表示する

## 各言語での実装

### C

FizzBuzz.c

```
#include <stdio.h>

int main(int argc, char *argv[]){
     for(int ii = 0; ii <= 100; ii++){
          if (ii % 15 == 0){
               printf("FizzBuzz\n");
          } else if (ii % 3 == 0) {
               printf("Fizz\n");
          } else if (ii % 5 == 0) {
               printf("Buzz\n");
          } else {
               printf("%d\n", ii);
          }
     };
     return 0;
}
```

```
$ gcc -v
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 7.0.0 (clang-700.0.72)
Target: x86_64-apple-darwin14.5.0
Thread model: posix
```
### C++

FizzBuzz.cpp:

```
#include <iostream>

using namespace std;

int main(int argc, char** argv){
     for(int ii = 0; ii <= 100; ii++){
          if (ii % 15 == 0){
               cout << "FizzBuzz\n";
          } else if (ii % 3 == 0) {
               cout << "Fizz\n";
          } else if (ii % 5 == 0) {
               cout << "Buzz\n";
          } else {
               cout << ii << "\n";
          }
     };
     return 0;
}
```


```
$ g++ --version
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 7.0.0 (clang-700.0.72)
Target: x86_64-apple-darwin14.5.0
Thread model: posix
```

### Java

FizzBuzz.java:

```
class FizzBuzz {
    public static void main (String[] args){
        for(int ii=0; ii <= 100; ii++){
            if (ii % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (ii % 3 == 0) {
                System.out.println("Fizz");
            } else if (ii % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(ii);
            }
        }
    }
}
```

```
$ java -version
java version "1.8.0_45"
Java(TM) SE Runtime Environment (build 1.8.0_45-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)
```
### Ruby

FizzBuzz.rb:

```
#! /usr/bin/env ruby
(0..100).each do |ii|
  msg = ""
  if ii % 3 == 0
    msg += "Fizz"
  end
  if ii % 5 == 0
    msg += "Buzz"
  end
  puts msg.empty? ? ii : msg
end
```

```
$ ruby -v
ruby 2.4.0dev (2016-10-02 trunk 56323) [x86_64-darwin14]
```

### Common Lisp

FizzBuzz.cl:

```
(loop for ii from 1 to 100 do
     (cond
       ((zerop (mod ii 15)) (print "FizzBuzz"))
       ((zerop (mod ii 3)) (print "Fizz"))
       ((zerop (mod ii 5)) (print "Buzz"))
       ((zerop 0) (print ii))
       ))
```

```
$ sbcl --version
SBCL 1.3.10
```

### Elixir

FizzBuzz.exs:

```
(1..100) |> Enum.each(fn (ii) -> cond do
    rem(ii, 15) === 0 -> IO.puts "FizzBuzz"
    rem(ii, 3) === 0 -> IO.puts "Fizz"
    rem(ii, 5) === 0 -> IO.puts "Buzz"
    true -> IO.puts ii
  end
end)
```

```
$ elixir -v
Erlang/OTP 19 [erts-8.1] [source] [64-bit] [smp:4:4] [async-threads:10] [hipe] [kernel-poll:false] [dtrace]

Elixir 1.3.4
```

### Go

FizzBuzz.go:

```
package main

import "fmt"

func main(){
	for ii := 1; ii < 101; ii++ {
		msg := ""
		if ii % 3 == 0 {
			msg += "Fizz"
		}
		if ii % 5 == 0 {
			msg += "Buzz"
		}
		if len(msg) == 0{
			fmt.Println(ii)
		}else{
			fmt.Println(msg)
		}
	}
}
```

```
$ go version
go version go1.7.1 darwin/amd64
```
### Python

FizzBuzz.py:

```
#! /usr/bin/env python
import itertools


for ii in itertools.count(1):
    msg = ''
    if ii % 3 == 0:
        msg += 'fizz'
    if ii % 5 == 0:
        msg += 'buzz'
    print(msg or ii)
```

```
$ python -V
Python 3.5.2 :: Continuum Analytics, Inc.
```




### Node.js

FizzBuzz.js:

```
for(var ii=1; true; ii++){
    var msg = "";
    if ((ii % 3) == 0){
        msg += "Fizz";
    }
    if ((ii % 5) == 0){
        msg += "Buzz";
    }
    console.log(msg || ii);
}

```

```
$ node -v
v6.7.0
```
### PHP

FizzBuzz.php:

```
<?php
for($ii = 0; $ii <= 100; $ii++){
    $msg = "";
    if ($ii % 3 == 0) {
        $msg .= "Fizz";
    }
    if ($ii % 5 == 0) {
        $msg .= "Buzz";
    }
    print (empty($msg) ? $ii : $msg) . "\n";
}
?>
```

```
$ php -v
PHP 5.5.27 (cli) (built: Jul 23 2015 00:21:59)
Copyright (c) 1997-2015 The PHP Group
Zend Engine v2.5.0, Copyright (c) 1998-2015 Zend Technologies
```
### Lua

FizzBuzz.lua:

```
for ii = 1, 100 do
   if ii % 15 == 0 then
      print("FizzBuzz")
   elseif ii % 3 == 0 then
      print("Fizz")
   elseif ii % 5 == 0 then
      print("Buzz")
   else
      print(ii)
   end
end
```

```
$ lua -v
Lua 5.2.4  Copyright (C) 1994-2015 Lua.org, PUC-Rio
```

### Perl

FizzBuzz.pl:

```
#! /usr/bin/env perl5
use strict;

for (my $ii = 0; $ii < 101; $ii++){
    if ($ii % 15 == 0) {
        print "FizzBuzz\n";
    } elsif ($ii % 3 == 0) {
        print "Fizz\n";
    } elsif ($ii % 5 == 0) {
        print "Buzz\n";
    } else {
        printf("%d\n", $ii);
    }
}
```

```
$ perl -v

This is perl 5, version 16, subversion 3 (v5.16.3) built for darwin-thread-multi-2level

Copyright 1987-2012, Larry Wall

Perl may be copied only under the terms of either the Artistic License or the
GNU General Public License, which may be found in the Perl 5 source kit.

Complete documentation for Perl, including FAQ lists, should be found on
this system using "man perl" or "perldoc perl".  If you have access to the
Internet, point your browser at http://www.perl.org/, the Perl Home Page.
```

### Cython

FizzBuzzCy.pyx:

```
cdef int ii = 0
for ii in range(1, 101):
    if ii % 15 == 0:
        print("FizzBuzz")
    elif ii % 3 == 0:
        print("Fizz")
    elif ii % 5 == 0:
        print("Buzz")
    else:
        print(ii)

```

```
$ cython --version
Cython version 0.24.1
$ python --version
Python 3.5.2 :: Continuum Analytics, Inc.
```

<!-- ### C# -->
### Objective-C

FizzBuzz.m:

```
#include <stdio.h>

int main(int argc, const char * argv[]){
     for(int ii = 0; ii <= 100; ii++){
          if (ii % 15 == 0){
               printf("FizzBuzz\n");
          } else if (ii % 3 == 0) {
               printf("Fizz\n");
          } else if (ii % 5 == 0) {
               printf("Buzz\n");
          } else {
               printf("%d\n", ii);
          }
     };
     return 0;
}
```

```
$ gcc -v
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 7.0.0 (clang-700.0.72)
Target: x86_64-apple-darwin14.5.0
Thread model: posix
```

### Swift

FizzBuzz.swift:

```
(1...100).map {(ii: Int) -> String in
    if ii % 15 == 0 {
        return "FizzBuzz"
    } else if ii % 3 == 0 {
        return "Fizz"
    } else if ii % 5 == 0 {
        return "Buzz"
    } else {
        return String(ii)
    }
}.forEach { (msg: String) in
    print(msg)
}
```

```
$ swiftc --version
Apple Swift version 2.0 (swiftlang-700.0.59 clang-700.0.72)
Target: x86_64-apple-darwin14.5.0
```
<!-- ### awk -->
<!-- ### jq -->
<!-- ### CSS -->
<!-- ### Erlang -->
<!-- ### Shell Script -->
<!-- ### アセンブリ(GAS) -->
<!-- ### アセンブリ(NASM) -->
<!-- ### アセンブリ(LLVM-IR) -->

## 所管

同じことを考えている人は結構いる。目的は違うかもしれないけど、やっていることは同じ。

- https://www.rosettacode.org/wiki/FizzBuzz

本当にこれをホワイトボードに書かせて一体何を判断するっていうんだ。
現状の言語の基本構文を理解しているかとかそんなことを気にしているんだろうか。
もう面倒なのでFizzBuzzのURLを名刺に貼っておこう。
