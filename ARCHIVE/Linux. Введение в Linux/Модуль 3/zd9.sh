#!bin/bash
# задача на функции
# калькулятор
# господа, у кого возникли трудности с "*" и "**" попробуйте передавать функции значения вот таким образом:
# calc "${a}" "${b}" "${c}"

calc () { # int digit, operand, int digit
    # let "a = $1" # error
    # let "op = $2" # error
    # let "b = $3" # error
    a=$1; op=$2; b=$3
    case $op in
        "-")
            let "res = a - b"
            echo "$res"
            ;;
        "+")
            let "res = a + b"
            echo "$res"
            ;;
        "*")
            let "res = a * b"
            echo "$res"
            ;;
        "/")
            let "res = a / b"
            echo "$res"
            ;;
        "%")
            let "res = a % b"
            echo "$res"
            ;;
        "**")
            let "res = a ** b"
            echo "$res"
            ;;
        *)
            res='error'
            echo "$res"
    esac
}

while true; do
    read digit1 operand digit2
    if [[ "exit" == $digit1 ]]; then echo "bye"; break; fi
    # calc $digit1 $operand $digit2 # error
    # calc ${digit1} ${operand} ${digit2} # error
    calc "${digit1}" "${operand}" "${digit2}"
    if [[ "error" == $res ]]; then break; fi
done

# calc $1 $2 $3 # error
# calc "${1}" "${2}" "${3}" # error
# echo "a = $a"
# echo "op = $op"
# echo "b = $b"
# echo "res = $res"