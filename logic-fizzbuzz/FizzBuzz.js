for(var ii=1; ii<101; ii++){
    var msg = "";
    if ((ii % 3) == 0){
        msg += "Fizz";
    }
    if ((ii % 5) == 0){
        msg += "Buzz";
    }
    console.log(msg || ii);
}
