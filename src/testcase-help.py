import argparse
import os
import glob
import chardet



def fix_encoding_file(file_path):
    '''
    Change file's encoding to UTF-8 LE (the UNIX standard)
    '''
    with open(file_path, "rb") as file:
        raw_data = file.read()
        detected_encoding = chardet.detect(raw_data)["encoding"]

    # Read the file with the detected encoding
    with open(file_path, "r", encoding=detected_encoding) as file:
        content = file.read()
    
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
    print(f"Fixing encoding of {args.path}")

    if args.dir:
        if not os.path.isdir(args.path):
            print(f"Error: {args.path} is not a valid directory!")
            return 1

        fix_encoding_dir(args.path, args.recursive)

    else:
        if not os.path.isfile(args.path):
            print(f"Error: {args.path} is not a valid file!")
            return 1

        fix_encoding_file(args.path)

    print("Success!")


def main():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("path", metavar="PATH", help="Path to a file or directory")

    arg_parser.add_argument(
        "-d", "--dir",
        action="store_true",
        help="Treat the path as a directory (default: treat as a file)"
    )

    arg_parser.add_argument(
        "-rec", "--recursive", 
        action="store_true", 
        help="Process directories recursively"
    )

    arg_parser.add_argument(
        "-fe", "--fix-encoding",
        action="store_true",
        help="fix encoding of file(s) to UTF-8 LF"
    )


    args = arg_parser.parse_args()


    if args.fix_encoding:
        if fix_encoding(args) == 1: return 1




if __name__ == "__main__":
    exit(main())