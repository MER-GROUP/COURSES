#!bin/bash
# НЕПРАВИЛЬНЫЙ ПРИМЕР !!!
# ЗНАКАМИ (==, <, И ТД.) СРАВНИВАЮТСЯ СТРОКИ
# ЧИСЛА СРАВНИВАЮТСЯ ЧЕРЕЗ СТРОКОВЫЕ ОПЕРАТОРЫ (-eq, lt и т.д.)
if [[ $1 == 0 ]]
then
    echo "No students"
elif [[ $1 == 1 ]]
then
    echo "$1 student"
elif [[ $1 < 5 ]]
then
    echo "$1 students"
elif [[ $1 > 4 ]]
then
    echo "A lot of students"
fi