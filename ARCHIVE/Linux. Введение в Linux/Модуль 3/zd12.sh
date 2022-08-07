#!bin/bash
while true; do
        read p1 p2 p3
        if [[ $p1 == "exit" ]]; then echo bye; exit; fi
        case $p2 in
                "+") echo $(( $p1 + $p3 ));;
                "-") echo $(( $p1 - $p3 ));;
                "*") echo $(( $p1 * $p3 ));;
                "/") echo $(( $p1 / $p3 ));;
                "%") echo $(( $p1 % $p3 ));;
                "**") echo $(( $p1 ** $p3 ));;
                *) echo error; exit;;
        esac
done