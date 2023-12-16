#!/usr/bin/env bash

echo "----------------------------------"

for arg in examples/*/*.out; do
	echo "${arg}"
    code=${arg/out/sh}
    echo "${code}"
    echo "copy: ${code} > ${arg}"
    echo ${PWD}

    # code2=${arg/out/red}
    # echo "${code2}"
    # p="maxredmax"
    # echo ${p}
    # echo "${p/red/ramanenka}"

    # ${code} > ${arg}
    # ${PWD}/${code} > ${PWD}/${arg}

    ${code} > ${arg}
    
    # cat "${code}"
    # # echo -e "\n"
    # # echo ""
    # echo
done

echo "----------------------------------"