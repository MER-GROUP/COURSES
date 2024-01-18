#!/usr/bin/env bash
echo "###################################"

FILE="vitkovskaja"
FILE2="VitkoVskaja"
FILE3="VitkoVskaja will be mariied with Ramanenka"

echo "This is FILE"
echo "This is $FILE"
echo "This is ${FILE}"
echo "This is ${#FILE}"

echo "###################################"

echo "This is ${##FILE}"
echo "This is ${##*/FILE}"
echo "This is ${FILE##*/}"

echo "###################################"

echo "\${0} = ${0}"
echo "usage: ${0##*/} namesfile datafile"
echo "usage: ${FILE##*/} namesfile datafile"
echo "usage: ${FILE##*V} namesfile datafile"
echo "usage: ${FILE##*Vitkov} namesfile datafile"
echo "usage: ${0##*/} namesfile datafile"

echo "###################################"

echo "usage: ${FILE#Vit} namesfile datafile"
echo "usage: ${FILE##Vit} namesfile datafile"
echo "usage: ${FILE#*Vit} namesfile datafile"
echo "usage: ${FILE##*Vit} namesfile datafile"

echo "###################################"

echo "usage: ${FILE#*k} namesfile datafile"
echo "usage: ${FILE##*k} namesfile datafile"

echo "###################################"

echo "usage: ${FILE%k*} namesfile datafile"
echo "usage: ${FILE%%k*} namesfile datafile"

echo "###################################"

echo "usage: ${FILE^} namesfile datafile"
echo "usage: ${FILE^^} namesfile datafile"

echo "###################################"

echo "usage: ${FILE2,} namesfile datafile"
echo "usage: ${FILE2,,} namesfile datafile"

echo "###################################"

declare -u UPPER=max
declare -l lower=MIN
echo "UPPER = ${UPPER}"
echo "lower = ${lower}"

echo "###################################"

echo "${FILE3/ /_}"
echo "${FILE3// /_}"
echo "${FILE3// /}"

echo "###################################"

echo "${FILE3:0:5}"
echo "${FILE3:1:5}"
echo "${FILE3:1}"

echo "###################################"