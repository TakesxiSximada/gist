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
