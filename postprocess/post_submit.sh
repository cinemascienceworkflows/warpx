#!/bin/bash

#BSUB -P <compute_allocation>
#BSUB -W 01:00
#BSUB -nnodes 1
#BSUB -J <pantheon_post_jid> 

pushd /sw/summit/paraview/spack-5.10.0 > /dev/null 2>&1
source share/spack/setup-env.sh
module load gcc/9.3.0
spack compiler add
spack load python;spack load py-numpy;spack load py-mpi4py;spack load py-pandas;spack load paraview
spack unload openssl
popd > /dev/null 2>&1

SCRIPT=<pantheon_run_dir>/tubesSummitCdb.py

jsrun -n 1 pvpython $SCRIPT > pvpython.output
