#!/usr/bin/env bash
echo "###################################"

FILE="Vitkovskaja"

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