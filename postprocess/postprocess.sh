#!/bin/bash

source ./pantheon/env.sh > /dev/null 2>&1

echo "----------------------------------------------------------------------"
echo "PTN: Post-processing"

# --------------------------------------------------------------------
# BEGIN: EDIT THIS SECTION
# copy executable and support files to the result directory
#     this step will vary, depending on the application requirements

cp postprocess/tubesSummitCdb.py $PANTHEON_RUN_DIR
cp postprocess/tubesSummit.pvsm $PANTHEON_RUN_DIR
cp postprocess/post_submit.sh $PANTHEON_RUN_DIR

mkdir -p $PANTHEON_RUN_DIR/cinema_databases

# END: EDIT THIS SECTION
# --------------------------------------------------------------------

# go to run dir and update the submit script
pushd $PANTHEON_RUN_DIR > /dev/null 2>&1

sed -i "s/<pantheon_workflow_jid>/${PANTHEON_WORKFLOW_JID}/" post_submit.sh
sed -i "s/<pantheon_post_jid>/${PANTHEON_POST_JID}/" post_submit.sh
sed -i "s#<pantheon_workflow_dir>#${PANTHEON_WORKFLOW_DIR}#" post_submit.sh
sed -i "s#<pantheon_run_dir>#${PANTHEON_RUN_DIR}#" post_submit.sh
sed -i "s#<compute_allocation>#${COMPUTE_ALLOCATION}#" post_submit.sh
sed -i "s#<pantheon_cdb>#${PANTHEON_CDB}#g" post_submit.sh

sed -i "s#<PvSkript>#${PANTHEON_RUN_DIR}/tubesSummit.pvsm#" tubesSummitCdb.py
sed -i "s#<DataDirectory>#${PANTHEON_RUN_DIR}/diags#" tubesSummitCdb.py
sed -i "s#<AMReXBoxLibGridReader3FileNames>#${PANTHEON_RUN_DIR}/diags/diag100240/#" tubesSummitCdb.py
sed -i "s#<CDB>#${PANTHEON_RUN_DIR}/cinema_databases/${PANTHEON_CDB}#" tubesSummitCdb.py

sed -i "s#<AMReXBoxLibGridReader3FileNames>#${PANTHEON_RUN_DIR}/diags/diag100240/#" tubesSummit.pvsm

# submit the job
echo "PTN: submitting run ..."
echo "----------------------------------------------------------------------"
bsub post_submit.sh
