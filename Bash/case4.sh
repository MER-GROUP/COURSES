#!/usr/bin/env bash
echo "###################################"

# case ${filename} in
case ${1} in
    ./* )
        echo -ne "local\n"
    ;&
    # [^/]* )
    111 )
        echo -ne "relative\n"
    ;;&
    /* )
        echo -ne "absolute\n"
    ;&
    */* )
        echo -ne "pathname\n"
    # ;;
    ;;&
    * )
        echo -ne "filename\n"
    ;;
esac

echo "###################################"