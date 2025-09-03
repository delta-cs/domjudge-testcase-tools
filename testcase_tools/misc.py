import subprocess, platform, os

class tcol:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

VERBOSE = False # global variable holding whether do verbose prints or not
verb_print = lambda message, col=tcol.ENDC: print(col+message+tcol.ENDC) if VERBOSE else None
cprint = lambda message, col=tcol.ENDC: print(col+message+tcol.ENDC)

SAMPLE_TEST_MARKER_FILE = ".issample"


#============================================================
# GENERAL
#============================================================


def open_in_text_editor(path :str):
    '''Tries to open <path> in a text editor'''
    editor = os.environ.get("EDITOR")
    if not editor:
        editor = "notepad" if platform.system() == "Windows" else "nano"

    subprocess.call([editor, path])

