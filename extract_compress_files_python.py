import os
import gzip
import sys
import shutil

def extract_files():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".gz"):
                with gzip.open(os.path.join(root, file), "rb") as comp_file:
                    with open(os.path.join(root, file).replace(".gz", ""), 'wb') as uncomp_file:
                        shutil.copyfileobj(comp_file, uncomp_file)
                os.remove(os.path.join(root, file))

def compress_files():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".vnnlib") or file.endswith(".onnx"):
                with open(os.path.join(root, file), 'rb') as uncomp_file:
                    with gzip.open(os.path.join(root, file) + ".gz", "wb") as comp_file:
                        shutil.copyfileobj(uncomp_file, comp_file)
                os.remove(os.path.join(root, file))

def main():
    if sys.argv[1] == "compress" or sys.argv[1] == "c" or sys.argv[1] == "comp":
        print("Compressing .vnnlib and .onnx files...")
        compress_files()
    else:
        print("Extracting .gz files...")
        extract_files()

if __name__ == "__main__":
    main()