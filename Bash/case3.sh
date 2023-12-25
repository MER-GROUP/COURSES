#!/usr/bin/env bash
echo "##################################"

echo "\${#} = ${#}"
# BOOK_ASC="~/WORK/PYTHON/LinuxTests/dir/" # error
# BOOK_ASC="/home/red/WORK/PYTHON/LinuxTests/dir/"
# BOOK_ASC="${HOME}/WORK/PYTHON/LinuxTests/dir/"
BOOK_ASC="${HOME}/WORK/PYTHON/MyPROG/COURSES/Bash/"
# cd ${BOOK_ASC}

echo "${BOOK_ASC}"

[ -n "${BOOK_ASC}" ] || {
	echo "FATAL: export \$BOOK_ASC to the location of the Asciidoc files!"
	exit 1
}

# cd "${BOOK_ASC}" || {
\cd "${BOOK_ASC}" || {
	echo "FATAL: can't cd to '$BOOK_ASC'!"
	exit 2
}

echo "##################################"

SELF=${0} # name of this script
echo "SELF is ${SELF}" # for test
action=${1} # first arg of this script
echo "action is ${action}" # for test
shift # shift all args of this script on the left

[ -x /usr/bin/xsel -a ${#} -lt 1 ] && {
	text=$( xsel -b )
	function Output { # args 
		echo -en "${*}" | xsel -bi
        echo -en "this is new text: ${*}\n" # for test
        echo -en "PWD is: $PWD \n" # for test
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
    h1 )
        # Output "[[ $( ${SELF} id ${text} ) ]]\n=== ${text}"
        # Output "[[$($SELF id $text)]]\n=== $text"
        # Output "[[$( id ${user} )]]\n=== ${text}" # for test

        # Output "[[$( pwd = ${pwd} )]]\n=== ${text}" # for test
        # echo "###############"
        # echo "SELF = ${SELF}"
        # echo "###############"
        # # echo "SELF = $( echo "${SELF} id ${text}" )"
        # # echo "SELF = $( echo "${SELF} id ${text}" )"
        # echo "SELF = $( echo ${SELF} id ${text} )"
        # echo "###############"

        # Output "[[ $( echo "${SELF} id ${text}" ) ]]\n=== ${text}"
        # Output "[[ $( echo ${SELF} id ${text} ) ]]\n=== ${text}"
        Output "[[ $( bash ${SELF} id ${text} ) ]]\n=== ${text}" # < ----- !!!

        # Output $( echo ${SELF} id ${text} )
        # Output $( ${SELF} id ${text} )
        # Output $( bash ${SELF} id ${text} ) # < ----- !!!!!
        # Output $( echo ${text} | tr -s '_' ' ' | tr '[:upper:]' '[:lower:]' | tr -d ':punct:' \
        #     | tr -s ' ' '_' )
    ;;
    h2 )
        Output "[[ $( ${SELF} id ${text} ) ]]\n==== ${text}"
    ;;
    h3 )
        Output "[[ $( ${SELF} id ${text} ) ]]\n==== ${text}"
    ;;
    
    # lists
    bul | bullet )
        # echo "This is bul" # for test
        Output "* ${text}"
    ;;
    nul | number | order* )
        Output ". ${text}"
    ;;
    term )
        Output "term_here::\n ${text}"
    ;;

    # paragraphs
    bold )
        Output "*${text}*"
    ;;
    i | italic* | itl )
        Output "_${text}_"
    ;;
    c | constant | cons )
        Output "+${text}+"
    ;;
    type | constantbold )
        Output "*+${text}+*"
    ;;
    var | constantitalic )
        Output "_++${text}++_"
    ;;
    sub | subscript )
        Output "~${text}~"
    ;;
    sup | superscript )
        Output "^${text}^"
    ;;
    foot )
        Output "footnote:[${text}]"
    ;;
    url | link )
        Output "link:\$\$${text}\$\$[]"
    ;;
    esc | escape )
        Output "\$\$${text}\$\$[]"
    ;;

    # tools
    id ) # tools
        Output $( echo ${text} | tr -s '_' ' ' | tr '[:upper:]' '[:lower:]' | tr -d ':punct:' \
            | tr -s ' ' '_' )
    ;;
    index ) # tools
        egrep '^=== ' ch*.asciidoc | egrep -v '^ch00.asciidoc' \
            > ${BOOK_ASC}/index.txt && {
                echo "Updated: ${BOOK_ASC}/index.txt"
                exit 0
            } || {
                echo "FAILED to update: ${BOOK_ASC}/index.txt"
                exit 1
            }
    ;;
    return ) # tools
        for output in examples/*/*.out; do
            code=${output/out/sh}
            echo "Re-running code for: ${code} > ${output}"
            ${code} > ${output}
        done
    ;;
    cleanup ) ## tools
        rm -fv {ch??,app?}.{pdf,xml,html} book.{xml,html} docbook-xsl.css
    ;;

    # other
	* ) ### other
		echo "Your arg is ${action}" # for test
        \cd -
        ( echo "Usage:" 
        egrep '\)[[:space:]]+#' $0 
        echo ''
        egrep '\)[[:space:]]+##' $0 
        echo ''
        egrep '\)[[:space:]]+###' $0 ) | grep "${1:-.}" | more
	;;
esac

echo "##################################"