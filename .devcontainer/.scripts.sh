#!/bin/bash
levels="1-easy 2-medium 3-hard"
i=1
for category in "$@" 
do
    basedir="$i-$category"
    for l in $levels; do
        mkdir -p $basedir/$l; touch $basedir/$l/.keep;
    done
    i=$((i + 1));
done
