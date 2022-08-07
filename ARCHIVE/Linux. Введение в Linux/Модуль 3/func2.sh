#!bin/bash
# пример использования функций

# функция
files_creator () { # dir_name file_name
    full_name=$1/$2
    if [[ ! -e $1 ]]; then
        echo "Dir is not exist, creating $1"
        mkdir $1
    elif [[ ! -d $1 ]]; then
        echo "$1 is not dir, exiting"
        exit 1
    fi
    touch $1/$2
} 

# программа
again="yes"
while [[ "yes" == $again ]]; do
    read -p "Enter dir and file names: " dir_name file_name
    files_creator $dir_name $file_name
    if [[ -f $full_name ]]; then echo "Created $full_name"; fi
    read -p "Again? (yes/no)" again
done