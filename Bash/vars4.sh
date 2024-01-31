#!/usr/bin/env bash
echo "###################################"

echo "\$RANDOM == ${RANDOM}"

echo "###################################"

declare -a mylist
mylist=(foo bar baz one two "three four")

echo "mylist = ${mylist}"
echo "mylist = ${mylist[@]}"

range=${#mylist[@]}
echo "\${#mylist[@]} == ${#mylist[@]}"
echo "\${#mylist[*]} == ${#mylist[*]}"

random=$(( $RANDOM % $range ))
echo "random = ${random}"

echo "range = ${range}, random = ${random}, choice = ${mylist[${random}]}"

echo "choice = ${mylist[$(( ${RANDOM} % ${#mylist[@]} ))]}"

echo "###################################"

echo "\$TMP == ${TMP}"

TEMP_DIR=./myscript.${RANDOM}
TEMP_DIR1=./myscript.${RANDOM}
TEMP_DIR2=./myscript.${RANDOM}
[ -d "${TEMP_DIR}" ] || mkdir "${TEMP_DIR}"
[[ -d "${TEMP_DIR1}" ]] || mkdir "${TEMP_DIR1}"
test -d "${TEMP_DIR2}" || mkdir "${TEMP_DIR2}"

echo "###################################"