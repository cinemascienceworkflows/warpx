#!/bin/bash

source ./pantheon/env.sh > /dev/null 2>&1

RUN_CLEAN=true

if $RUN_CLEAN; then
    echo "----------------------------------------------------------------------"
    echo "PTN: cleaning results directory ..." 
    echo "----------------------------------------------------------------------"

    rm -rf $PANTHEON_RUN_DIR
    mkdir $PANTHEON_RUN_DIR
fi

# --------------------------------------------------------------------
# BEGIN: EDIT THIS SECTION
# copy executable and support files to the result directory
#     this step will vary, depending on the application requirements

# copy inputs
cp run/submit.sh $PANTHEON_RUN_DIR
cp inputs/warpx/input.file $PANTHEON_RUN_DIR 
cp inputs/warpx/warpx.profile $PANTHEON_RUN_DIR 
# copy the executable
cp $PANTHEON_WORKFLOW_DIR/warpx/build/bin/warpx.3d.MPI.CUDA.DP.OPMD.QED $PANTHEON_RUN_DIR/warpx

# END: EDIT THIS SECTION
# --------------------------------------------------------------------

# go to run dir and update the submit script
pushd $PANTHEON_RUN_DIR > /dev/null 2>&1
sed -i "s/<pantheon_workflow_jid>/${PANTHEON_WORKFLOW_JID}/g" submit.sh
sed -i "s#<pantheon_workflow_dir>#${PANTHEON_WORKFLOW_DIR}#g" submit.sh
sed -i "s#<pantheon_run_dir>#${PANTHEON_RUN_DIR}#g" submit.sh
sed -i "s#<compute_allocation>#${COMPUTE_ALLOCATION}#g" submit.sh
sed -i "s#<pantheon_cdb>#${PANTHEON_CDB}#g" submit.sh

# submit the job
echo "----------------------------------------------------------------------"
echo "PTN: submitting run ..." 
echo "----------------------------------------------------------------------"
bsub submit.sh
