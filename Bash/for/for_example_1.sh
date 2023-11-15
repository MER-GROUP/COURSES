echo "----------------------------------"

for (( i=0; i<10; i++ )); do
	printf '%d\n' "${i}"
done

echo "----------------------------------"

for args; do
	echo "${args}"
done
echo "FUNCNAME == ${FUNCNAME[0]}"
echo "arg 0 == ${0}"
echo "arg 1 == ${1}"
echo "arg 2 == ${2}"
echo "${*}"
echo "${@}"

echo "----------------------------------"

i=0
for (( ; ; )); do
	if test 10 -eq ${i}; then
		break
	fi
	printf '%d\n' "${i}"
	(( i++ ))
done

echo "----------------------------------"

function example {
	for args; do
		echo "${args}"
	done
	echo "FUNCNAME == ${FUNCNAME[0]}"
	echo "arg 0 == ${0}"
	echo "arg 1 == ${1}"
	echo "arg 2 == ${2}"
	echo "${*}"
	echo "${@}"
}
example max red fire

echo "----------------------------------"