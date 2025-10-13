from testcase_tools.misc import *

import chardet
import glob
import os


#============================================================
# FIX ENCODING
#============================================================

def fix_encoding_file(file_path):
    '''
    Change file's encoding to UTF-8 LE (the UNIX standard)
    '''
    verb_print(f"  fixing encoding of {file_path}")

    with open(file_path, "rb") as file:
        raw_data = file.read()
        detected_encoding = chardet.detect(raw_data)["encoding"]

    # Read the file with the detected encoding
    try:
        with open(file_path, "r", encoding=detected_encoding) as file:
            content = file.read()
    except:
        verb_print(f"ERROR: skipping \"{file_path}\", the file could not be processed!")
        return 1
    
    # Normalize line endings to LF and prepare UTF-8 content
    normalized_content = content.replace("\r\n", "\n").replace("\r", "\n")

    if len(normalized_content) > 0 and normalized_content[-1] != '\n': normalized_content += '\n' # ensure the file always ends with \n
    
    # Write the file back with UTF-8 encoding
    with open(file_path, "w", encoding="utf-8", newline="\n") as file:
        file.write(normalized_content)



def fix_encoding_dir(path, recursive=False, safe=True):
    '''
    Change all contained files encoding to UTF-8 LE (the UNIX standard)
    '''

    for f in glob.glob(f"{path}/**", recursive=recursive):
        if(os.path.isfile(f) and ((not safe) or any(x not in f for x in ('in.', 'out.')))): # if is file and has in/out in name
            fix_encoding_file(f)



def fix_encoding(path :str, recursive=False, safe=True):
    verb_print(f"TASK: fix encoding of {path}", tcol.HEADER)

    
    if os.path.isdir(path):
        verb_print(f"  directory detected, processing")
        fix_encoding_dir(path, recursive, safe=True)


    elif os.path.isfile(path):
        fix_encoding_file(path)

    else:
        cprint(f"Error: {path} is not a valid file or directory!", tcol.FAIL)
        return 1


    verb_print("TASK DONE", tcol.HEADER)
