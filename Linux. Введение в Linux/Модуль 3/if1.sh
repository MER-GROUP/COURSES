#!/bin/bash
echo "Hi!"

# если количество введенных аргументов меньше 2
if [[ $# -lt 2 ]]
then
    echo "You should specify at least two arguments!"
    exit
fi

# если первый аргумент не путь или не файл
if [[ !(-e $1) || !(-f $1) ]]
then
    echo "File $1 doesn't exist or is not a file!"
    exit
fi

# скопировать аргумент 1 в аргумент 2
cp $1 $2
echo "Copied $1 to $2!"