#! /bin/bash

#
# CK installation script
#
# See CK LICENSE for licensing details.
# See CK COPYRIGHT for copyright details.
#

# PACKAGE_DIR
# INSTALL_DIR
# CPANM_URL
# CPANM_PACKAGE

######################################################################################

echo "Installing cpanm from ${CPANM_URL} as ${CPANM_PACKAGE} package"

${CK_ENV_TOOL_WGET_BIN_FULL} -O - "${CPANM_URL}" | perl - "${CPANM_PACKAGE}"

if [ "${?}" != "0" ] ; then
  echo "Error: installation failed!"
  exit 1
fi

