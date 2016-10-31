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