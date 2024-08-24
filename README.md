# fullyconnected_benchmarks_vnncomp

## Overview

This repository is a collection of fully connected benchmarks from VNNCOMP 2022-2024. The aim is to provide a more organized version of the existing benchmarks to facilitate the testing of new software.

Each directory contains a single benchmark and is organized as follows:

* onnx: This directory contains the neural networks, and it may have subdirectories.
* vnnlib: This directory contains the unsafety properties, and it may have subdirectories.
* instances.csv: This file specifies, in each line, a network, a property, and optionally a timeout.
* README.md: This file may optionally include an extract from the original README and a link to the benchmark's original repository. It also lists all the networks in the /onnx directory, detailing the number of parameters and the node types within the networks.

Due to the large file sizes in this repository, all files have been compressed. Git and GitHub have limitations on file sizes they can handle, so to manage this, we have compressed the files to facilitate proper version control, storage, and download speed. Additional information about file decompression can be found in the general repositiory [benchmarks_vnncomp](https://github.com/AndyVale/benchmarks_vnncomp)