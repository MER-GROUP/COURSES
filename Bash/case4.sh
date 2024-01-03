#!/usr/bin/env bash
echo "###################################"

# case ${filename} in
case ${1} in
    ./* )
        echo -ne "local"
    ;&
    [^/]* )
        echo -ne "relative\n"
    ;;&
    /* )
        echo -ne "absolute"
    ;&
    */* )
        echo -ne "pathname"
    ;;
    * )
        echo -ne "filename"
    ;;
esac

echo "###################################"