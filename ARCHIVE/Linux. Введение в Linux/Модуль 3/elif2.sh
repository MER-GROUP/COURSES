#!bin/bash
if [[ -f $1 ]]
then
    echo "Removing file"
    rm $1
elif [[ -d $1 ]]
    echo "removing dir"
    rm -r $1
else
    echo "Can't remove $1"
fi