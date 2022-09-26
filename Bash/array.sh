#!/bin/bash
array=(первый второй третий четвертый пятый)
for i in ${array[@]}; do
    echo $i
done