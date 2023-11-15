echo "----------------------------------"

for num in 1 2 3 4 5; do
	echo "${num}"
done

echo "----------------------------------"

for person in Max Red Mom Dad; do
	echo "${person}"
done

echo "----------------------------------"

a=5
name=Ramanenka
for person in Max 1 Red ${a} Mom ${name} Dad 3; do
	echo "${person}"
done

echo "----------------------------------"

for arg in $( ls | sort -ur ); do
	echo "${arg}"
done

echo "----------------------------------"

for arg in $( cat file.txt ); do
	echo "${arg}"
done

echo "----------------------------------"

for arg in $( < file.txt ); do
	echo "${arg}"
done

echo "----------------------------------"

for arg in $( find . -name '*.txt' ); do
	echo "${arg}"
done

echo "----------------------------------"

for arg in $( find . -type d | LC_ALL=C sort ); do
	echo "${arg}"
done

echo "----------------------------------"

for arg in $( seq 1 10 ); do
	echo "${arg}"
done
echo "${arg}"

echo "----------------------------------"

for (( i=1; i<=10; i++ )); do
	echo "${i}"
done
echo "${i}"

echo "----------------------------------"

for arg in {1..10}; do
	echo "${arg}"
done
echo "${arg}"

echo "----------------------------------"

for arg in {1..10..2}; do
	echo "${arg}"
done
echo "${arg}"

echo "----------------------------------"

for arg in {01..10}; do
	echo "${arg}"
done
echo "${arg}"

echo "----------------------------------"

for arg in {1..05}; do
	echo "${arg}"
done
echo "${arg}"

echo "----------------------------------"

for arg in file{1..05}.txt; do
	echo "${arg}"
done
echo "${arg}"

echo "----------------------------------"
echo file{1..05}.txt
echo "----------------------------------"
for arg in file{1..05}.txt; do
	printf '%s\n' "${arg}"
done
echo "${arg}"
echo "----------------------------------"

for arg in {1..5..2}; do
	echo "${arg}"
done
echo "${arg}"

echo "----------------------------------"

for arg in $( seq 1 0.2 2 ); do
	echo "${arg}"
done
echo "${arg}"

echo "----------------------------------"

for arg in $( seq 2.1 0.3 3.2 ); do
	echo "${arg}"
done
echo "${arg}"

echo "----------------------------------"