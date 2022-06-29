#!bin/bash
# пример использования внешних программ в bash
# и кодов возврата программ

# if `program > some_file.txt`
if `pwd > out.txt`
then
    echo "if pwd == 0 : $?"
else
    echo "if pwd == 1 : $?"
fi

# Сначала запустить program, затем if [[ $? -eq 0 ]]