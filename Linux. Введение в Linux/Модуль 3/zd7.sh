#!bin/bash
# задача на функции
# Вычисление НОД (наибольший общий делитель) с помощью алгоритма Евклида

gcd () {  # takes M and N arguments
  M=$1; N=$2
  if [[ M -eq N ]]; then
    echo "GCD is $M"
    # return
  elif [[ M -gt N ]]; then
    let "M -= N"
    gcd $M $N
  else
    let "N -= M"
    gcd $M $N
  fi
} 

# ввод переменных с клавиатуры
read var1 var2

# выполнять покуда строки var1 var2 не пустые 
while [[ -n $var1 && -n $var2 ]]; do
  # запуск функции
  gcd $var1 $var2
  # ввод переменных с клавиатуры
  read var1 var2
done

# сообщение
echo "bye"