from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path as osp
import sys

def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)

this_dir = osp.dirname(__file__)
# lib_path = osp.join(this_dir, 'all_lib/lib_new_attention')
lib_path = osp.join(this_dir, 'all_lib/lib_org_backbone')
add_path(lib_path)
# /media/data/maleilei/MLIC/CCD_MLIC

# /media/data/maleilei/MLICdataset