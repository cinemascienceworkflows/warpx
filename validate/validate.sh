#!/bin/bash

source ./pantheon/env.sh > /dev/null 2>&1


OUTPUT=$PANTHEON_RUN_DIR/cinema_databases/$PANTHEON_CDB
GOLD=validate/data/pantheon.cdb

echo "----------------------------------------------------------------------"
echo "PTN: validating $OUTPUT" 

imgs="RenderView1_000000p=000.00t=180.00.png RenderView1_000000p=180.00t=180.00.png RenderView1_000000p=300.00t=180.00.png"

PASS=true
if [ -d $OUTPUT ]; then
    for val in $imgs; do
        if cmp "$OUTPUT/$val" "$GOLD/$val"; then
            echo "     Comparing images $OUTPUT/$val"
            echo "                      $GOLD/$val"
        else
            echo "FILES differ:"
            echo "    $OUTPUT/$val"
            echo "    $GOLD/$val"
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

