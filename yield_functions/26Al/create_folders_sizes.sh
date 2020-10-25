#!/bin/bash

mkdir H
mkdir L
mkdir LL

for comp in H L LL; do
	for (( j = 5 ; j <= 250; j += 5 )) ; do
  		mkdir -p $comp/"${j}cm"
	done
done