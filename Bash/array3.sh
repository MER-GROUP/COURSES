#!/bin/bash

# сделаем скрипт, который будет выводить все файлы из указанной директории, 
# которые имеют права доступа 755:

ERR=27
EXT=0

if [ $# -ne 1 ]; then
    echo "Используйте: $0 <путь>"
    exit $ERR
fi

if [ ! -d $1 ]; then
    echo "Каталог $1 не существует"
    exit $ERR
fi

temp=( $(find $1 -maxdepth 1 -type f) )

for i in "${temp[@]}"; do
    perm=$(ls -l $i)
    if [ `expr ${perm:0:10} : "-rwxr-xr-x"` -eq 10 ]; then
        echo ${i##*/}
    fi
done

exit $EXT