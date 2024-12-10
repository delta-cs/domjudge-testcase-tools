# domjudge-testcase-tools
**The tool provides:**
- enforcing correct file encodings (UTF-8 LF)
- generation / verification of correctness of testcases
- creating zip files for simple upload of problem to DOMjudge

## usage
```
usage: testcase-tools.py [-h] [-V] [-r] [-f] [-g CMD] [-v CMD] [-z] [-n NAME] PATH

positional arguments:
  PATH                  Path to a file or directory

options:
  -h, --help            show this help message and exit
  -V, --verbose         enable verbose output
  -r, --recursive       process directories recursively
  -f, --fix-encoding    fix encoding of file(s) to UTF-8 LF
  -g CMD, --generate-answers CMD
                        run CMD on every in.txt and generate out.txt
  -v CMD, --verify-answers CMD
                        run CMD for in.txt and verify correctness of out.txt
  -z, --make-zip        create mass upload zip from directory
  -n NAME, --name NAME  specify name for zip
```