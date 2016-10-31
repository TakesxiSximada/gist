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
