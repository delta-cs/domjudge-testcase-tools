import os
import subprocess
import time
import glob
from testcase_tools.misc import *

#============================================================
# GENERATE / CHECK
#============================================================


def gen_check_res(tests_path :str, cmd :str, gen=False, exit_with_errors=False, timeout=None):
    '''
    Run command on all in files, write output to ans or verify if ans is matching
    '''
    cprint(f"TASK: {(lambda: 'generating' if gen else 'verifying')()} results", tcol.HEADER)

    if timeout is not None: timeout = float(timeout)

    tests_failed = 0
    runs_failed = 0
    timeouts = 0
    tests_total = 0

    test_i = 1
    for in_file in glob.glob(f"**/in.*", root_dir=tests_path, recursive=True):
        tests_total += 1
        in_file_path = os.path.join(tests_path, in_file)

        dir_path = os.path.join(tests_path, os.path.dirname(in_file))
        dir_name = os.path.basename(dir_path)

        if(os.path.isfile(os.path.join(dir_path, ".testignore"))):
            cprint(f"ignoring test {dir_name}", tcol.WARNING)
            continue

        with open(in_file_path, "r") as f:
            in_txt = f.read()


        cprint(f"  running {cmd} on {dir_path}")

        try:
            start_time = time.time()
            process = subprocess.run(
                cmd,
                input=in_txt,
                text=True, # Treat input and output as strings
                capture_output=True, # Capture stdout and stderr
                shell=True,
                timeout=timeout
            )
            delta_time = time.time() - start_time

            cprint(f"  finished in: {delta_time} s", tcol.OKBLUE)
        except subprocess.TimeoutExpired:
            cprint(f"Error: timeout hit ({timeout}s)", tcol.FAIL)
            timeouts += 1
            continue

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
                cprint(f"  answer in {dir_name} matching", tcol.OKGREEN)
        
        test_i += 1

    cprint(f"TASK DONE, {tests_failed + runs_failed + timeouts}/{tests_total} tests failed ({runs_failed} run errors, {timeouts} timeouts)", tcol.HEADER)

    if exit_with_errors:
        if runs_failed > 0: exit(8)
        if timeouts > 0: exit(6)
        if tests_failed > 0: exit(4)
