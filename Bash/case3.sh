#!/usr/bin/env bash
echo "##################################"

echo "\${#} = ${#}"
# BOOK_ASC="~/WORK/PYTHON/LinuxTests/dir/" # error
# BOOK_ASC="/home/red/WORK/PYTHON/LinuxTests/dir/"
BOOK_ASC="${HOME}/WORK/PYTHON/LinuxTests/dir/"
# cd ${BOOK_ASC}

echo "${BOOK_ASC}"

[ -n "${BOOK_ASC}" ] || {
	echo "FATAL: export \$BOOK_ASC to the location of the Asciidoc files!"
	exit 1
}

\cd "${BOOK_ASC}" || {
	echo "FATAL: can't cd to '$BOOK_ASC'!"
	exit 2
}

echo "##################################"

SELF=${0} # name of this script
action=${1} # first arg of this script
shift # shift all args of this script on the left

[ -x /usr/bin/xsel -a ${#} -lt 1 ] && {
	text=$( xsel -b )
	function Output { # args 
		echo -en "${*}" | xsel -bi
	}
} || {
	text=${*}
	function Output { # args 
		echo -en "${*}"
	}
}

echo "##################################"

case ${action} in
    # headers
    h1)
        Output "[[ $( ${SELF} id ${text} ) ]]\n=== ${text}"
        # Output "[[$($SELF id $text)]]\n=== $text"
    ;;
    h2)
        Output "[[ $( ${SELF} id ${text} ) ]]\n==== ${text}"
    ;;
    h3)
        Output "[[ $( ${SELF} id ${text} ) ]]\n==== ${text}"
    ;;
    # lists
	*)
		#
	;;
esac

echo "##################################"