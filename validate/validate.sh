#!/bin/bash

source ./pantheon/env.sh > /dev/null 2>&1


OUTPUT=$PANTHEON_RUN_DIR/cinema_databases/$PANTHEON_CDB
GOLD=validate/data/pantheon.cdb

echo "----------------------------------------------------------------------"
echo "PTN: validating $OUTPUT" 

imgs="0.png 10.png 20.png 30.png"

PASS=true
if [ -d $OUTPUT ]; then
    for val in $imgs; do
        if cmp "$OUTPUT/$val" "$GOLD/$val"; then
            echo "     Comparing images $GOLD/$val"
        else
            echo "FILES differ:"
            echo "    $OUTPUT"
            echo "    $GOLD"
            PASS=false
        fi
    done
else
    echo "Cinema Database: $OUTPUT does not exist"
    PASS=false
fi

if $PASS; then
    echo "PTN: PASS"
    echo "----------------------------------------------------------------------"
else
    echo "PTN: FAIL"
    echo "----------------------------------------------------------------------"
    exit 1
fi

