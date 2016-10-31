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
