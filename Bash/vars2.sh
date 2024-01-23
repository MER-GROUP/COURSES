#!/usr/bin/env bash
echo "###################################"

customer_subnet_name='Acme Inc subnet 10.11.12.13/24'

echo ''
echo "Say we have  this string: ${customer_subnet_name}"
echo ''

customer_name=${customer_subnet_name%subnet*}
subnet=${customer_subnet_name##* }
ipa=${customer_subnet_name%/*}
cidr=${customer_subnet_name#*/}
fw_object_name1=${customer_subnet_name// /_}
fw_object_name2=${customer_subnet_name//\//-}
# fw_object_name2=${customer_subnet_name////-}
fw_object_name3=${customer_subnet_name,,}

echo ${customer_name}
echo ${subnet}
echo ${ipa}
echo ${cidr}
echo ${fw_object_name1}
echo ${fw_object_name2}
echo ${fw_object_name3}

echo "###################################"