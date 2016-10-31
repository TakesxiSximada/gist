for ii in `seq 1 100`
do
    if (expr $ii % 15) == 0
    then
        echo $ii
    fi

done
