# domjudge-testcase-tools
Tooling for checking correct file encodings, and correctness of testcases

## usage
```
usage: testcase-help.py [-h] [-V] [-r] [-f] [-g CMD] [-c CMD] PATH

positional arguments:
  PATH                  Path to a file or directory

options:
  -h, --help            show this help message and exit
  -V, --verbose         enable verbose output
  -r, --recursive       process directories recursively
  -f, --fix-encoding    fix encoding of file(s) to UTF-8 LF
  -g CMD, --generate-results CMD
                        run CMD on every in.txt and generate out.txt
  -c CMD, --check-results CMD
                        run CMD for in.txt and verify correctness of out.txt
```