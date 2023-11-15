echo "----------------------------------"

arr=(qqq www eee rrr)
echo "${arr[@]}"
echo "${arr[*]}"
echo "${arr}"
echo "${!arr[*]}"
echo "${!arr[@]}"

echo "----------------------------------"

# for el in ${arr[*]}; do
for el in ${arr[@]}; do
	echo "${el}"
done

echo "----------------------------------"

declare -A hash
while read key value; do
	# if test -z ${key}; then
	if [[ -z ${key} ]]; then
		break
	fi
	hash[$key]="${value}"
	# echo "111 ${!hashone[*]}"
	# echo "222 ${hashone[${key}]}"
done

for key in ${!hash[@]}; do
	echo "key = ${key} and value = ${hash[${key}]}"
done

# read key value
# hash[${key}]=${value}
# echo "${!hash[*]} and ${hash[${key}]}"
echo "----------------------------------"

declare -A hash2
while read word count; do
	if [[ -z ${word} ]]; then
		break
	fi
	let hash2[$word]+="${count}"
done

for word in ${!hash2[@]}; do
	echo "word = ${word} and count = ${hash2[${word}]}"
done
echo "----------------------------------"