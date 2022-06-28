#!bin/bash
# пример использования внешних программ в bash
# и кодов возврата программ

cd ~
if `pwd`
then
    echo "if pwd == 0 : $?"
else
    echo "if pwd == 1 : $?"
fi