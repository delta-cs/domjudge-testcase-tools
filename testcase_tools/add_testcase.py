from testcase_tools.misc import *

import os, shutil

#============================================================
# ADD TESTCASE
#============================================================

def add_testcase(tests_path, testcase_name, is_sample=False, in_fp:str=None, out_fp:str=None, blank=False):
    '''
    Generate a new testcase, open text editor for in/out
    '''
    testcase_path = os.path.join(tests_path, testcase_name)

    # make folder
    os.mkdir(testcase_path)

    in_path = os.path.join(testcase_path, "in.txt")
    out_path = os.path.join(testcase_path, "out.txt")


    if in_fp is not None:
        shutil.copyfile(in_fp, in_path)
    else:
        open(in_path, "w").close()

        if not blank:
            open_in_text_editor(in_path)

        
    if out_fp is not None:
        shutil.copyfile(out_fp, out_path)
    else:
        open(out_path, "w").close()
        
        if not blank: 
            open_in_text_editor(out_path)

    if is_sample:
        open(os.path.join(testcase_path, SAMPLE_TEST_MARKER_FILE), "w").close()