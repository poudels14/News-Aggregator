#!/bin/bash

for i in `seq 1 $2`
do
	echo "Downloading Page$i"
	wget -O "./$1/page$i.html" "https://news.ycombinator.com/news?p=$i"
done
