#!bin/bash
# пример использования арифметики в переменных

exp=0
base=10
while [[ $exp -le 5 ]]
do
    let "result = base ** exp"
    echo "$base^$exp = $result"
    let "exp += 1"
done