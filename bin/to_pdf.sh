#!/usr/bin/env bash

if [ $# -ne 1 ]; then 
    echo "usage: $0 FILE"
    exit
fi

input=$1
# remove extension
name=$(echo ${input} | sed s/.md$//)
output=${name}.pdf

pandoc -V geometry:margin=1cm -r markdown -o ${output} ${input}
