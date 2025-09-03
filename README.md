# domjudge-testcase-tools
**The tool provides:**
- enforcing correct file encodings (UTF-8 LF)
- generation / verification of correctness of testcases
- creating zip files for simple upload of problem to DOMjudge
- ... and more

## installation
- *a)* to install without cloning, run:
   ```bash
   pip install git+https://github.com/delta-cs/domjudge-testcase-tools.git
   ```

- *b)* if you have cloned the repo, you can install by running:
   ```bash
   pip install -e . # replace '.' with root directory of the repo if needed
   ```


## usage
```bash
$ testcase-tools [-h | --help] [-V | --verbose] [option]
```
Options:
*`[option]`*| *description*
--|--
`package` | package problem into zip archive for domjudge
`add` | initialize new testcase
`normalize` | normalize testcases text files to `UTF-8 LF`
`run` | run solution on all testcases - useful for testing solutions or generating expected outputs

Arguments for all options can be shown by runnnig:
```bash
$ testcase-tools [option] -h
```


## tests directory format
format of directory containing tests assumed by this toolkit
```sh
<tests directory>
├─ <testcase name / description>
│  ├─ in.txt
│  ├─ out.txt
│  └╶ .issample # OPTIONAL, presence of .issample marks sample testcase
├─ ...
```

```sh
# example
tests/
├─ 01-sample-test/
│  ├─ in.txt
│  ├─ out.txt
│  └─ .issample
│
└─ 02-hidden-test/
   ├─ in.txt
   └─ out.txt
```
