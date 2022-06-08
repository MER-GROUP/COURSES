#!bin/bash
if [[ $1 -eq 0 ]]
then
    echo "No students"
elif [[ $1 -eq 1 ]]
then
    echo "$1 student"
elif [[ $1 -lt 5 ]]
then
    echo "$1 students"
else
    echo "A lot of students"
fi