#!bin/bash
# пример использования арифметики в переменных

var=1 + 1
echo "$var" # error

var=1+1
echo "$var" # no math

let var = 1 + 1
echo "$var" # error

let var=1+1
echo "$var"

let "var = 1 + 1"
echo "$var"