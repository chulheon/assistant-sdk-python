#!/bin/bash

#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
# set me
FILES=/home/pi/chulheon/telegram/iu/*
for f in $FILES
    do
        echo "$f"
        omxplayer "$f"
done
# restore $IFS
IFS=$SAVEIFS