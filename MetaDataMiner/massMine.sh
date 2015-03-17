#/bin/bash

SCREEN_FLAGS="-dm -L -s /bin/bash -S"
SCREEN_COM=/usr/bin/screen

for i in `seq 1 $2`;
do
	$SCREEN_COM $SCREEN_FLAGS "$1$i" python "$1_com.py"
done  
