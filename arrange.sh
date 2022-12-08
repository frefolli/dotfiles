#!/bin/bash

function cleanRepository () {
    if [ -d ./repository ]; then
        rm -r ./repository
    fi
    mkdir ./repository
    echo "packages:" > ./repository/index.yml
}

function arrangePackage () {
    file=$1
    tar cf $file.tar $file
    gzip $file.tar
    mkdir ../repository/$file -p
    mv $file.tar.gz ../repository/$file/default.tar.gz
    echo "- $file" >> ../repository/index.yml
}

function arrangeRepository () {
    cleanRepository
    cd ./sources
    for file in $(find * -prune -type d); do
        arrangePackage $file
    done
    cd ..
}

arrangeRepository
