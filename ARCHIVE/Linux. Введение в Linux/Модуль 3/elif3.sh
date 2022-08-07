#!bin/bash
# пример ветвления с if-elif-else
if [[ $1 -gt 5 ]]
then
  echo "one" 
elif [[ $1 -lt 3 ]]
then
  echo "two"
elif [[ $1 -eq 4 ]]
then
  echo "three"
else
  echo "four"
fi