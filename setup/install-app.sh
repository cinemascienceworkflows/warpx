# build and install the application

APP_COMMIT=0e809732a2ef032801ee9a64b5266edcd75a0213

# make a lower case version of the package 
APPDIR=`echo "$PANTHEON_APP" | awk '{print tolower($0)}'`

echo ----------------------------------------------------------------------
echo "PTN: building $PANTHEON_APP"
echo ----------------------------------------------------------------------

cp inputs/warpx/warpx.profile  $PANTHEON_WORKFLOW_DIR
pushd $PANTHEON_WORKFLOW_DIR > /dev/null 2>&1

git clone https://github.com/ECP-WarpX/WarpX.git $APPDIR
pushd $APPDIR > /dev/null 2>&1
git checkout $APP_COMMIT
popd > /dev/null 2>&1
source warpx.profile

echo ----------------------------------------------------------------------
echo "PTN: building $PANTHEON_APP"
echo ----------------------------------------------------------------------

pushd $APPDIR > /dev/null 2>&1
rm -rf build
cmake -S . -B build -DWarpX_OPENPMD=ON -DWarpX_DIMS=3 -DWarpX_COMPUTE=CUDA
cmake --build build -j 6

