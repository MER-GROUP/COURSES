echo "----------------------------------"

for file in *.jpeg; do
# for file in $(ls *.jpeg); do
	# echo "file = ${file}"
	# echo mv -v ${file} ${file}
	# echo mv -v ${file} ${file/JPEG/jpg/}
	# mv -v ${file} ${file/JPEG/jpg/}
	mv -v ${file} ${file/jpg/JPEG/}
done

echo "----------------------------------"

for node in web-server{00..09}; do
	# echo ssh ${node} 'echo -e "${HOSTNAME}\t$(date "+%F") $(uptime)"'
	echo -e "${HOSTNAME}\t$(date "+%F") $(uptime)"
done

echo "----------------------------------"

i=5
while test 0 -ne ${i}; do
	echo "${i}"
	(( i-- ))
done 

echo "----------------------------------"

i=5
! while test 0 -ne ${i}; do
	echo "${i}"
	(( i-- ))
done 

echo "----------------------------------"

i=5
until test 0 -eq ${i}; do
	echo "${i}"
	(( i-- ))
done 

echo "----------------------------------"