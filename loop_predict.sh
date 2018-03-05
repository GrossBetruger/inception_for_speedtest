#!/bin/bash
for i in $( ls $1 ); do
FULL_PATH=$1$i;
echo "image: $FULL_PATH";
python predict.py models/11_classes_retrained $FULL_PATH;
done
