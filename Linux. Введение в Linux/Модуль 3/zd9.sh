#!bin/bash
# задача на функции
# калькулятор

calc () { # int digit, operand, int digit
    # let "a = $1" # error
    # let "op = $2" # error
    # let "b = $3" # error
    a=$1; op=$2; b=$3
    case $op in
        "-")
            let "res = a + b"
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

calc $1 $2 $3
echo "a = $a"
echo "op = $op"
echo "b = $b"
echo "res = $res"