#!/usr/bin/env bash
VERSION='v1.2b'
echo "##################################"

function usage_exit { # no args
	# ${0} is the name of script 
	echo "${0} [color|last|len|long]"
	exit
}

echo "##################################"

function ls_length { # here's args
	# ${@} is the all of args this func
	ls -1 "${@}" | while read fn; do
		printf '%3d %s \n' ${#fn} ${fn}
	done | sort -n
	# echo "args of func = ${@}" 
}

function ls_length_2 { # here's args
	# ${@} is the all of args this func
	for args; do
		printf '%3d %s \n' ${#args} ${args}
	done | sort -n
	# echo "args of func = ${@}" 
}

echo "##################################"

function shift_func { # here's args
	# ${1}, ${2}, etc is the all of args this func
	echo "\${1} = ${1}"
	echo "\${2} = ${2}"
	shift
	echo "\${1} = ${1}"
	echo "\${2} = ${2}"
} 

echo "##################################"

# ${#} is count of args
echo "count of args is ${#}"
# if the count of arguments is less than 1, then exit the script
(( ${#} < 1 )) && usage_exit

echo "##################################"

# test of function ls_length 
# ls_length qwery red alert
# ls_length
ls_length case2.sh case.sh

# ls_length_2 qwery red alert
# ls_length_2
ls_length_2 case2.sh case.sh

echo "##################################"

# $1 is a first arg of this script
# $2 is a second arg of this script
sub=${1}
echo "sub = ${sub}"
echo "\${1} = ${1}"
echo "\${2} = ${2}"
shift
echo "\${1} = ${1}"
echo "\${2} = ${2}"

echo "##################################"

shift_func 111f 222f 333f 444f 555g

echo "##################################"

case ${sub} in
	color )
		pwd_color=$( pwd )
		echo "\$pwd_color = ${pwd_color}"
		# ls -N --color=tty -T 0 "${@}"
		ls -N --color=tty -T 0 ${pwd_color}
	;;
	last | latest )
		ls -lrt | tail "-n${1:-5}"
	;;
	len* )
		ls_length "${@}"
	;;
	long )
		ls_length "${@}" | tail -1
	;;
	* )
		echo "unknown command: ${sub}"
		usage_exit
	;;
esac

echo "##################################"