#!bin/bash
# задача на функции

counter ()  # takes one argument
{
  local let "c1+=$1"
  let "c2+=${1}*2"
} 

step=1
while [[ $step -le 10 ]]; do
  counter $step
  echo "counters are $c1 and $c2"
  let "step += 1"
done

echo "counters are $c1 and $c2"