# fullyconnected_benchmarks_vnncomp

## Overview

Due to the large file sizes in this repository, all files have been compressed. Git and GitHub have limitations on file sizes they can handle, so to manage this, we have compressed the files to facilitate proper version control and storage (and download speed).

## Decompressing Files

To work with the files, you will need to decompress them first. Below are the instructions for decompressing the files on both Linux and Windows systems.

### Linux

To decompress the files in the root directory and all subdirectories, run the following command in this directory:

```bash
gunzip * -r
```

### Windows

For Windows users, unfortunately, we have not found any built-in functionality, so we decided to use 7-Zip to decompress all files. We have provided a batch file to automate the decompression process using 7-Zip. Note that you need to add 7-Zip to your environment variables or modify the .bat file as specified in it. Once you have everything set up, simply execute the extract_files_windows.bat file located in this directory.

### Windows Alternative

You might already have software that allows your Windows PC to run Unix commands (e.g., Git Bash). If so, you can use those tools to decompress the files as you would on a Linux system.