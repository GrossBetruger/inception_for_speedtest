#!/bin/bash

inptdir=$1
splitsize=$2
dumpdir=$3

for i in $(seq $splitsize); do
	mkdir "$dumpdir/splited_$i" && 
	for fname in $(ls $inptdir | shuf -n $splitsize); do
		echo $fname 
		mv $inptdir$fname "$dumpdir/splited_$i/"
	done;
done	

