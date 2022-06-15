#!/bin/bash -l

# adding comment

source ./pantheon/env.sh > /dev/null 2>&1

echo "PTN: Establishing Pantheon workflow directory:"
echo "     $PANTHEON_WORKFLOW_DIR"

PANTHEON_SOURCE_ROOT=$PWD

# these settings allow you to control what gets built ...
BUILD_CLEAN=false
INSTALL_SPACK=false
USE_SPACK_CACHE=true
INSTALL_APP=false

# spack data
# SPACK_COMPILER_MODULE=gcc/9.3.0
# SPACK_COMPILER_MODULE=gcc/10.2.0
SPACK_COMMIT=4c6564f10aa516bc00c1d7dbfdeafe35128985fe
SPACK_NAME=e4s_pantheon
SPACK_CACHE_URL=https://cache.e4s.io/pantheon

# ---------------------------------------------------------------------------
#
# Build things, based on flags set above
#
# ---------------------------------------------------------------------------

START_TIME=$(date +"%r %Z")
echo ----------------------------------------------------------------------
echo "PTN: Start time: $START_TIME"
echo ----------------------------------------------------------------------

# if a clean build, remove everything
if $BUILD_CLEAN; then
    echo ----------------------------------------------------------------------
    echo "PTN: clean build ..."
    echo ----------------------------------------------------------------------

    if [ -d $PANTHEON_WORKFLOW_DIR ]; then
        rm -rf $PANTHEON_WORKFLOW_DIR
    fi
    if [ ! -d $PANTHEON_PATH ]; then
        mkdir $PANTHEON_PATH
    fi
    if [ ! -d $PANTHEON_PROJECT_DIR ]; then
        mkdir $PANTHEON_PROJECT_DIR
    fi
    mkdir -p $PANTHEON_WORKFLOW_DIR
    mkdir $PANTHEON_DATA_DIR
    mkdir $PANTHEON_RUN_DIR
fi

if $INSTALL_SPACK; then
    echo ----------------------------------------------------------------------
    echo "PTN: installing Spack ..."
    echo ----------------------------------------------------------------------

    pushd $PANTHEON_WORKFLOW_DIR > /dev/null 2>&1
    git clone https://github.com/spack/spack
    pushd spack > /dev/null 2>&1
    git checkout $SPACK_COMMIT
    popd > /dev/null 2>&1
    popd > /dev/null 2>&1
fi

# activate spack
pushd $PANTHEON_WORKFLOW_DIR > /dev/null 2>&1
. spack/share/spack/setup-env.sh

if $USE_SPACK_CACHE; then
    echo ----------------------------------------------------------------------
    echo "PTN: using Spack E4S cache ..."
    echo ----------------------------------------------------------------------

    # make sure correct mirror is used
    spack mirror remove $SPACK_NAME
    spack mirror add $SPACK_NAME $SPACK_CACHE_URL

    spack buildcache keys -it
    module load patchelf
fi

# install application 
spack install warpx@22.06 dims=3 compute=cuda

popd

# build the application and parts as needed
if $INSTALL_APP; then
    echo ----------------------------------------------------------------------
    echo "PTN: installing app ..."
    echo ----------------------------------------------------------------------

    source $PANTHEON_SOURCE_ROOT/setup/install-app.sh
fi

END_TIME=$(date +"%r %Z")
echo ----------------------------------------------------------------------
echo "PTN: statistics"
echo "PTN: start: $START_TIME"
echo "PTN: end  : $END_TIME"
echo ----------------------------------------------------------------------

