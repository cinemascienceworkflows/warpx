#!/bin/bash

source ./pantheon/env.sh > /dev/null 2>&1

echo "----------------------------------------------------------------------"
echo "PTN: Post-processing" 
echo "     packaging up cinema database to:" 

pushd $PANTHEON_RUN_DIR > /dev/null 2>&1

TARNAME=cinema_databases
echo "     $PANTHEON_DATA_DIR/${TARNAME}.tar.gz" 
echo "----------------------------------------------------------------------"

tar -czvf ${TARNAME}.tar.gz $TARNAME > /dev/null 2>&1
mv ${TARNAME}.tar.gz $PANTHEON_DATA_DIR

popd > /dev/null 2>&1


