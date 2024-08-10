# fullyconnected_benchmarks_vnncomp

## Overview

This repository is a collection of fully connected benchmarks from VNNCOMP 2022-2024. The aim is to provide a more organized version of the existing benchmarks to facilitate the testing of new software.

Each directory contains a single benchmark and is organized as follows:

* onnx: This directory contains the neural networks, and it may have subdirectories.
* vnnlib: This directory contains the unsafety properties, and it may have subdirectories.
* instances.csv: This file specifies, in each line, a network, a property, and optionally a timeout.
* README.md: This file may optionally include an extract from the original README and a link to the benchmark's original repository. It also lists all the networks in the /onnx directory, detailing the number of parameters and the node types within the networks.

Due to the large file sizes in this repository, all files have been compressed. Git and GitHub have limitations on file sizes they can handle, so to manage this, we have compressed the files to facilitate proper version control, storage, and download speed.

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