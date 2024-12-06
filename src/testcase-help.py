import argparse
import os
import glob
import chardet

VERBOSE = False # global variable holding whether do verbose prints or not
verb_print = lambda message: print(message) if VERBOSE else None




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
    
    # Write the file back with UTF-8 encoding
    with open(file_path, "w", encoding="utf-8", newline="\n") as file:
        file.write(normalized_content)



def fix_encoding_dir(path, recursive=False):
    '''
    Change all contained files encoding to UTF-8 LE (the UNIX standard)
    '''
    for f in glob.glob(f"{path}/**", recursive=recursive):
        if(os.path.isfile(f)):
            fix_encoding_file(f)



def fix_encoding(args :argparse.Namespace):
    verb_print(f"TASK: fix-encoding of {args.path}")

    
    if os.path.isdir(args.path):
        verb_print(f"  directory detected, processing")
        fix_encoding_dir(args.path, args.recursive)


    elif os.path.isfile(args.path):
        fix_encoding_file(args.path)

    else:
        print(f"Error: {args.path} is not a valid file or directory!")
        return 1


    verb_print("TASK DONE!")




def main():
    global VERBOSE
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("path", metavar="PATH", help="Path to a file or directory")

    arg_parser.add_argument(
        "-V", "--verbose",
        action="store_true",
        help="enable verbose output"
    )
    arg_parser.add_argument(
        "-r", "--recursive", 
        action="store_true", 
        help="process directories recursively"
    )
    arg_parser.add_argument(
        "-f", "--fix-encoding",
        action="store_true",
        help="fix encoding of file(s) to UTF-8 LF"
    )
    arg_parser.add_argument(
        "-g", "--generate-results",
        metavar="CMD",
        help="run CMD on every in.txt and generate out.txt"
    )
    arg_parser.add_argument(
        "-c", "--check-results",
        metavar="CMD",
        help="run CMD for in.txt and verify correctness of out.txt"
    )
    


    args = arg_parser.parse_args()

    VERBOSE = args.verbose


    if args.fix_encoding:
        if fix_encoding(args) == 1: return 1




if __name__ == "__main__":
    exit(main())