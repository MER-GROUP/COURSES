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

# ...

echo "###################################"