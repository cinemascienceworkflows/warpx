#!/bin/bash

#BSUB -P <compute_allocation> 
#BSUB -W 01:00
#BSUB -nnodes 1
#BSUB -J <pantheon_post_jid> 

module load paraview

SCRIPT=<pantheon_run_dir>/tubesSummitCdb.py

jsrun -n 1 pvpython $SCRIPT > pvpython.output
