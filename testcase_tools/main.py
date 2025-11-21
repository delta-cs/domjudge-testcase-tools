#!/usr/bin/env python3

import argparse


from testcase_tools import misc
from testcase_tools import package_problem
from testcase_tools import normalization
from testcase_tools import add_testcase
from testcase_tools import generate_verify

def tst(tests_path :str, name :str):
    print(tests_path, name)

def command_package(args):
    '''
    Namespace(verbose=False, option='package', tests_path='.', output='a.zip', name='unnamed problem', statement=None, timelimit=None, func=<function command_package at 0x75b06cbad120>)
    '''
    package_problem.make_import_zip(
        tests_path = args.tests,
        output_path = args.output,
        problem_name = args.name,
        statement_file = args.statement,
        timelimit = args.timelimit
    )


def command_normalize(args):
    normalization.fix_encoding(
        path=args.path,
        recursive=args.recursive,
        safe=args.safe_mode
    )
    

def command_add(args):
    add_testcase.add_testcase(
        tests_path = args.tests,
        testcase_name = args.name,
        is_sample = args.sample,
        out_fp = args.out,
        in_fp = args.inp,
        blank = args.blank
    )
    '''
    Namespace(verbose=False, option='add', tests='.', name='.', sample=False, in=None, out=None, blank=False, func=<function command_add at 0x7ac3c96c1440>)
    '''

def command_run(args):
    generate_verify.gen_check_res(
        tests_path = args.tests,
        cmd = args.cmd,
        gen = args.generate,
        exit_with_errors = args.exit_with_errors
    )
    '''
    Namespace(verbose=False, option='run', cmd='.', generate=False, func=<function command_run at 0x7998f52c14e0>)
    '''


def main():
    parser = argparse.ArgumentParser(
        prog="testcase-tools",
        description="Tools for managing and packaging domjudge problems",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-V", "--verbose",
        action="store_true",
        help="enable verbose output"
    )

    # SUBPARSERS =======================
    subparsers = parser.add_subparsers(
        title="available command options",
        dest="command",
        required=True
    )


    # PACKAGING ====================================
    command_package_parser = subparsers.add_parser(
        "package",
        help="package problem into .zip archive"
    )
    command_package_parser.add_argument(
        "tests",
        help="Path to directory containing tests"
    )
    command_package_parser.add_argument(
        '-o', '--output',
        default="a.zip",
        help="output filepath"
    )
    command_package_parser.add_argument(
        '-n', '--name',
        default="unnamed problem",
        help="name of problem"
    )
    command_package_parser.add_argument(
        '-s', '--statement',
        help="problem statement path (.pdf, .html, ...)"
    )
    command_package_parser.add_argument(
        '-t', '--timelimit',
        help="set problem timelimit"
    )
    command_package_parser.set_defaults(func=command_package)

    # ADD TESTCASE ====================================
    command_add_testcase_parser = subparsers.add_parser(
        "add",
        help="add new testcase"
    )
    command_add_testcase_parser.add_argument(
        "tests",
        help="Path to directory containing tests"
    )
    command_add_testcase_parser.add_argument(
        "name",
        help="name of the testcase"
    )
    command_add_testcase_parser.add_argument(
        '-s', '--sample',
        action="store_true",
        help="testcase is marked as sample if enabled"
    )
    command_add_testcase_parser.add_argument(
        '--inp',
        help="input file"
    )
    command_add_testcase_parser.add_argument(
        '--out',
        help="expected output file"
    )
    command_add_testcase_parser.add_argument(
        '-b', '--blank',
        action="store_true",
        help="leaves output files specified by --in and --out blank ; othervise text editor is opened"
    )
    command_add_testcase_parser.set_defaults(func=command_add)

    # NORMALIZATION ====================================
    command_normalize_parser = subparsers.add_parser(
        "normalize",
        help="normalize file encodings to UTF-8 LF"
    )
    command_normalize_parser.add_argument(
        "path",
        help="path to dir/file to normalized"
    )
    command_normalize_parser.add_argument(
        '-r', '--recursive',
        action="store_true",
        help="descend trough folders recursively"
    )
    command_normalize_parser.add_argument(
        '-s', '--safe-mode',
        action="store_true",
        help="will only attempt to convert files that contain 'in.*' or 'out.*' in their name"
    )
    command_normalize_parser.set_defaults(func=command_normalize)

    # RUNNING ====================================
    command_run_parser = subparsers.add_parser(
        "run",
        help="run testcases trough program"
    )
    command_run_parser.add_argument(
        "tests",
        help="Path to directory containing tests"
    )
    command_run_parser.add_argument(
        'cmd',
        help="command to run (ex. \"python solution.py\")"
    )
    command_run_parser.add_argument(
        '-g', '--generate',
        action="store_true",
        help="generate ans files for all in files; othervise verification is done on in + out pairs"
    )
    command_run_parser.add_argument(
        '-E', '--exit-with-errors',
        action="store_true",
        help="exits with code 4 if 1 or more tests are not matching, 8 on command exiting with non zero code"
    )
    command_run_parser.set_defaults(func=command_run)

    #==============================================

    args = parser.parse_args()
    misc.VERBOSE = args.verbose # set global VERBOSE (used by verbose print)

    # dispatch command handler function
    args.func(args)





if __name__ == "__main__":
    exit(main())
    