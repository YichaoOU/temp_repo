#!/bin/bash



pairs=$1
n=$2

# gunzip $pairs.gz

N_header=$(grep -r "^[#]" $pairs| wc -l)

head -n $N_header $pairs > $pairs.header

N_next_rows=$(expr $N_header + 1)

tail -n +$N_next_rows $pairs > $pairs.reads

LINES=$(wc -l $pairs.reads| awk '{ print $1 }')

frac=$(expr $LINES / $n)

shuf -n $frac $pairs.reads > $pairs.subsampled.reads

cat $pairs.header $pairs.subsampled.reads > $pairs.$n.subsampled

bgzip -f $pairs.$n.subsampled

# pairix -f $prefix.subsampled.gz

rm $pairs.header
rm $pairs.reads
rm $pairs.subsampled.reads



