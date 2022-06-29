#!bin/bash
# пример использования функций

# функция сложения
print_sum () { let "sum = $1 + $2"; echo "$1 + $2 = $sum"; }
# функция умножения
print_mult () { let "mult = $1 * $2"; echo "$1 * $2 = $mult"; }

# вызовы функций
print_sum 2 2
print_mult 5 5
print_mult 6 6