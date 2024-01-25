#!/usr/bin/env bash
echo "###################################"

LEN=${1:-5}
echo "LEN = ${LEN}"

echo "###################################"

for fn in * ; do
    # echo "${fn}"
    S=${LIST:+,}
    LIST="${LIST}${S}${fn}"
done
echo "${LIST}"

echo "###################################"

# perem="PEREM"
echo "perem = ${perem:="PEREM2"}"

echo "###################################"