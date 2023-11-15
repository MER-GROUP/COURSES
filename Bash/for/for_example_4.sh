echo "----------------------------------"

namelist=( Red Alert Max Payne Fire Srorm )
for person in ${namelist[@]}; do
	echo ${person}
done

echo "----------------------------------"

namelist2=( "Red Alert" "Max Payne" "Fire Srorm" )
for person in ${namelist2[@]}; do
	echo ${person}
done

echo "----------------------------------"

namelist3=( "Red Alert" "Max Payne" "Fire Srorm" )
for person in "${namelist3[@]}"; do
	echo ${person}
done
echo "${namelist3[@]}"

echo "----------------------------------"

namelist4=( Red Alert Max Payne Fire Srorm )
for person in ${namelist4[*]}; do
	echo ${person}
done

echo "----------------------------------"

namelist5=( "Red Alert" "Max Payne" "Fire Srorm" )
for person in ${namelist5[*]}; do
	echo ${person}
done

echo "----------------------------------"

namelist6=( "Red Alert" "Max Payne" "Fire Srorm" )
for person in "${namelist6[*]}"; do
	echo ${person}
done
echo "${namelist6[*]}"

echo "----------------------------------"