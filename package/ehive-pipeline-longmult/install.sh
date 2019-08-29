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

echo "Creating ${PIPECONFIG_CLASS} pipeline sqlite3 database"

init_pipeline.pl "${_PIPECONFIG_CLASS}" --pipeline_url "sqlite:///${INSTALL_DIR}/${_SQLITE_FILE}"

if [ "${?}" != "0" ] ; then
  echo "Error: installation failed!"
  exit 1
fi
