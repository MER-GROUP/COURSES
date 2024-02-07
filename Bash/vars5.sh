#!/usr/bin/env bash
echo "###################################"

my_file="$PWD/test.txt"
unique_lines_in_file="$(sort -u "${my_file}" | wc -l)"
echo "unique_lines_in_file = ${unique_lines_in_file}"

echo "###################################"

for arg in $(cat ${my_file}); do
    echo "arg = ${arg}"
done

echo "###################################"

for arg in $(< ${my_file}); do
    echo "arg = ${arg}"
done

echo "###################################"