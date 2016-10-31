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
