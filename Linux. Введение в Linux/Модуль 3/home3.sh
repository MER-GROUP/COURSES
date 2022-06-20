#!bin/bash

for str in a , b , c_d
do
  echo "start"  
  if [[ $str > "c" ]]
  then
    echo "$str > c"
    continue
  fi
  echo "finish"
done