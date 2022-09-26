#!/bin/bash
echo "Введите элементы массива:"
read -a array
echo "Результат:"
for i in ${array[@]}; do
    echo $i
done