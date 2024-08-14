import os
import gzip
import sys
import shutil
import argparse

def extract_files():
    '''Extracts all .gz files in the current directory'''
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".gz"):
                with gzip.open(os.path.join(root, file), "rb") as comp_file:
                    with open(os.path.join(root, file).replace(".gz", ""), 'wb') as uncomp_file:
                        shutil.copyfileobj(comp_file, uncomp_file)
                os.remove(os.path.join(root, file))

def compress_files():
    '''Compresses all .vnnlib and .onnx files in the current directory'''
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".vnnlib") or file.endswith(".onnx"):
                with open(os.path.join(root, file), 'rb') as uncomp_file:
                    with gzip.open(os.path.join(root, file) + ".gz", "wb") as comp_file:
                        shutil.copyfileobj(uncomp_file, comp_file)
                os.remove(os.path.join(root, file))

def main():
    parser = argparse.ArgumentParser(
    prog='extract_compress_files_python',
    description=
"""
------------------------------------------------------------------------------------------------------
This script will recursively extract .gz files and compress .vnnlib and .onnx files in the current directory.

To extract .gz files, use the extract mode.
To compress .vnnlib and .onnx files, use the compress mode.

examples:
    python extract_compress_files_python.py --mode extract
    python extract_compress_files_python.py --mode compress

or using the short versions:
    python extract_compress_files_python.py -m e
    python extract_compress_files_python.py -m c
""",
    epilog=
"""Thank you for using the script! :)
------------------------------------------------------------------------------------------------------""",
    formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('-m', '--mode', type=str, help='Mode: compress or extract', required=True)
    args = parser.parse_args()
    if args.mode == "compress" or args.mode == "c":
        print("Compressing .vnnlib and .onnx files...")
        compress_files()
    elif args.mode == "extract" or args.mode == "e":
        print("Extracting .gz files...")
        extract_files()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()