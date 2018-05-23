#!/usr/bin/env bash

DIR=$(dirname "${BASH_SOURCE[0]}")

if [ $# -ne 1 ]; then 
    echo "usage: $0 FILE"
    exit
fi

input=$1
# remove extension
name=$(echo ${input} | sed s/.md$//)
output=${name}.pdf
metadata_tmpl=${DIR}/metadata.yml
metadata=${DIR}/.metadata.yml

# config
margin=1cm
fontsize=14pt

# create metadata file
# TODO: move margin config to metadata file
cat ${metadata_tmpl} |
    sed s/_FONTSIZE_/${fontsize}/ \
    > ${metadata}

# generate pdfs
pandoc -V geometry:margin=${margin} \
       -r markdown \
       -o ${output} ${input} ${metadata}

# remove metadata file
rm ${metadata}
