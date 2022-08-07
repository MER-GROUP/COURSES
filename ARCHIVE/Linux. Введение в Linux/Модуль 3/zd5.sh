#!bin/bash
# пример использования внешних программ в bash
# и кодов возврата программ

echo "-------------------------"

if [[ 'string' ]] # 1 - True
then
  echo "success"  # output
else
  echo "fail"
fi

echo "-------------------------"

if [[ `pwd` ]]  # 1 - True
then
  echo "success"  # output
else
  echo "fail"
fi

echo "-------------------------"

if `pwd`  # 0 - True
then
  echo "success"
else
  echo "fail"    # output
fi

echo "-------------------------"