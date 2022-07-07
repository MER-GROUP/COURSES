#!bin/bash
while [[ True ]]
do
        read a b c
        if [[ "$a" != "exit" && -z "$b" ]]; then echo "error"; break; fi
        if [[ "$a" == "exit" ]]; then echo "bye"; break; fi
        let res=$a"$b"$c
        echo $res
done