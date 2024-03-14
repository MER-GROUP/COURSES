#!/usr/bin/env bash
echo "###################################"

echo "Hello 1"
# sleep 0.25
# sleep 0.5
# sleep 2.5
# sleep $((2 * 0.25)) # error
# sleep 2 * 0.25 # error
sleep $(awk 'BEGIN { print (1 * 0.25) }')
echo "Hello 2 and $(awk 'BEGIN { a = 6; b = 2; print (a + b) }')" 
echo "Hello 2 and $(awk 'BEGIN { print (1 * 0.25) }')" 
echo "Hello 2 and $(echo "1 * 0.25" | bc)" 
echo "Hello 2 and $((1 * 25))" 

echo "###################################"

for ((i=0; i<5; i++)); do
    echo "HI ${i}"
done

echo "###################################"

max=$((66 + 9 - 7 * 2 / 4))
echo ${max}

echo "###################################"

one=1
two=2
item=$((one + two))
echo ${item}

echo "###################################"

el=100
x=5
if ((el - 3 > x * 5)); then
    echo hello world
fi

echo "###################################"

echo $((5 > 2))
echo $((5 < 2))

echo "###################################"

step=1
((step++))
echo ${step}

echo "###################################"

((median = step * 4))
echo ${median}

echo "###################################"

((median *= 2))
echo ${median}
echo ${?}

echo "###################################"

# $((step++))

echo "###################################"

let "step++"
echo ${step}

echo "###################################"

let "median = median * 4"
echo ${median}

echo "###################################"

let "median *= 4"
echo ${median}

echo "###################################"

let step++
echo ${step}

echo "###################################"

# let median *= 4 # error
# echo ${median}

echo "###################################"