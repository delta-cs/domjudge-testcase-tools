import os
import subprocess
import time
import glob
from testcase_tools.misc import *

#============================================================
# GENERATE / CHECK
#============================================================


def gen_check_res(tests_path :str, cmd :str, gen=False, exit_with_errors=False):
    '''
    Run command on all in files, write output to ans or verify if ans is matching
    '''
    verb_print(f"TASK: {(lambda: "generating" if gen else "verifying")()} results", tcol.HEADER)

    tests_failed = 0
    runs_failed = 0

    test_i = 1
    for in_file in glob.glob(f"**/in.*", root_dir=tests_path, recursive=True):

        in_file_path = os.path.join(tests_path, in_file)

        dir_path = os.path.join(tests_path, os.path.dirname(in_file))
        dir_name = os.path.basename(dir_path)

        with open(in_file_path, "r") as f:
            in_txt = f.read()


        verb_print(f"  running {cmd} on {dir_path}")

        start_time = time.time()
        process = subprocess.run(
            cmd,
            input=in_txt,
            text=True, # Treat input and output as strings
            capture_output=True, # Capture stdout and stderr
            shell=True
        )
        delta_time = time.time() - start_time

        verb_print(f"  finished in: {delta_time} s", tcol.OKBLUE)

        if process.returncode != 0:
            cprint(f"Error: '{cmd}' failed on '{in_file_path}' with exit code {process.returncode}", tcol.FAIL)
            runs_failed += 1

        out_txt = process.stdout
        

        if gen:
            verb_print("  writing out.txt")
            with open(f"{dir_path}/out.txt", "w") as f:
                f.write(out_txt)

        else:
            verb_print("  searching for out file to compare")

            out_files = glob.glob("out.*", root_dir=dir_path)

            if len(out_files) != 1:
                cprint(f"Error: missing out file in {dir_path}", tcol.FAIL)
                tests_failed += 1
                continue

            with open(f"{dir_path}/{out_files[0]}", "r") as f:
                orig_out_txt = f.read()
            
            if out_txt != orig_out_txt:
                cprint(f"VERIFICATION ERROR: answer in \"{dir_name}\" does NOT Match answer generated with \"{cmd}\"", tcol.FAIL + tcol.BOLD)
                tests_failed += 1
            else:
                verb_print(f"  answer in {dir_name} matching", tcol.OKGREEN)
        
        test_i += 1

    verb_print(f"TASK DONE, {tests_failed} tests failed, {runs_failed} run errors", tcol.HEADER)

    if exit_with_errors:
        if runs_failed > 0: exit(8)
        if tests_failed > 0: exit(4)
