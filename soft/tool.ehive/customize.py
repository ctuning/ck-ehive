#
# Collective Knowledge (individual environment - setup)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#

import os
import sys

##############################################################################

def version_cmd(i):
    beekeeper_full_path     = i['full_path']

    version_cmd     = beekeeper_full_path + " --version | head -1 | awk '{print $2}' >$#filename#$"

    return {'return':0, 'cmd':version_cmd}


##############################################################################

def setup(i):
    """
    Input:  {
              cfg              - meta of this soft entry
              self_cfg         - meta of module soft
              ck_kernel        - import CK kernel module (to reuse functions)

              host_os_uoa      - host OS UOA
              host_os_uid      - host OS UID
              host_os_dict     - host OS meta

              target_os_uoa    - target OS UOA
              target_os_uid    - target OS UID
              target_os_dict   - target OS meta

              target_device_id - target device ID (if via ADB)

              tags             - list of tags used to search this entry

              env              - updated environment vars from meta
              customize        - updated customize vars from meta

              deps             - resolved dependencies for this soft

              interactive      - if 'yes', can ask questions, otherwise quiet
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              bat          - prepared string for bat file
            }

    """


    # Get variables
    ck=i['ck_kernel']

    iv=i.get('interactive','')

    cus=i.get('customize',{})

    hosd=i['host_os_dict']
    tosd=i['target_os_dict']

    winh=hosd.get('windows_base','')

    full_path               = cus.get('full_path','')
    path_scripts            = os.path.dirname(full_path)
    path_repo_root          = os.path.dirname(path_scripts)
    path_modules            = os.path.join(path_repo_root, 'modules')

    env                     = i['env']
    env['PERL5LIB']         = path_modules + ( ';%PERL5LIB%' if winh=='yes' else ':${PERL5LIB}')
    env['PATH']             = path_scripts + ( ';%PATH%' if winh=='yes' else ':${PATH}')

    env_prefix                  = cus['env_prefix']
    env[env_prefix+'_ROOT']     = path_repo_root
    env[env_prefix+'_SCRIPTS']  = path_scripts
    env[env_prefix+'_MODULES']  = path_modules

    return {'return':0, 'bat':''}
