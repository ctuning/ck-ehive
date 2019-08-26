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
    cpanm_full_path = i['full_path']

    version_cmd     = cpanm_full_path + " --version | head -1 | cut -d ' ' -f 4 >$#filename#$"

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
    path_bin                = os.path.dirname(full_path)

    # FIXME: assuming cpanm is installed in user's home

    path_perl5_root         = os.path.dirname(path_bin)
    path_perl5_lib          = os.path.join(path_perl5_root, 'lib', 'perl5')

    env                     = i['env']
    env['PERL5LIB']         = path_perl5_lib + ( ';%PERL5LIB%' if winh=='yes' else ':${PERL5LIB}')
    env['PATH']             = path_bin + ( ';%PATH%' if winh=='yes' else ':${PATH}')

    env_prefix                  = cus['env_prefix']
    env[env_prefix+'_ROOT']     = path_perl5_root
    env[env_prefix+'_BIN']      = path_bin
    env[env_prefix+'_PERL5LIB'] = path_perl5_lib

    return {'return':0, 'bat':''}
