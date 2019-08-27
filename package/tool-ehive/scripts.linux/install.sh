#! /bin/bash

#
# CK installation script
#
# See CK LICENSE for licensing details.
# See CK COPYRIGHT for copyright details.
#

# PACKAGE_DIR
# INSTALL_DIR

######################################################################################

echo "Installing eHive's Perl dependencies using cpanm"

"${CK_ENV_CPANM_BIN_FULL}" --force B::Keywords

"${CK_ENV_CPANM_BIN_FULL}" --installdeps --with-recommends "${INSTALL_DIR}/${PACKAGE_SUB_DIR}"


if [ "${?}" != "0" ] ; then
  echo "Error: installation failed!"
  exit 1
fi

