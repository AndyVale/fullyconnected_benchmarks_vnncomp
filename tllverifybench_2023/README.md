# <a href = "https://github.com/jferlez/TLLVerifyBench">TLL Verify Bench</a>
Proposed by: James Ferlez (University of California, Irvine)

## Motivation
This benchmark consists of Two-Level Lattice (TLL) NNs, which have been shown to be amenable to fast verification algorithms (e.g. FerlezKS22). Thus, this benchmark was proposed as a means of comparing TLL-specific verification algorithms with general-purpose NN verification algorithms (i.e. algorithms that can verify arbitrary deep, fully-connected ReLU NNs).

## Networks
The networks in this benchmark are a subset of the ones used in Experiment 3 of FerlezKS22. Each of these TLL NNs has `n=2` inputs and `m=1` output. The architecture of a TLL NN is further specified by two parameters: `N`, the number of local linear functions, and `M`, the number of selector sets. This benchmark contains TLLs of sizes `N = M = 8, 16, 24, 32, 40, 48, 56, 64`, with `30` randomly generated examples of each (the generation procedure is described in Section 6.1.1 of FerlezKS22). At runtime, the specified verification timeout determines how many of these networks are included in the benchmark so as to achieve an overall 6-hour run time; this selection process is deterministic. Finally, a TLL NN has a natural representation using multiple computation paths Figure 1 of FerlezKS22, but many tools are only compatible with fully-connected networks. Hence, the ONNX models in this benchmark implement TLL NNs by "stacking" these computation paths to make a fully connected NN (leading to sparse weight matrices: i.e. with many zero weights and biases). The `TLLnet` class (https://github.com/jferlez/TLLnet) contains the code necessary to generate these implementations via the `exportONNX` method.

## Specifications
All specifications have as input constraints the hypercube `[-2,2]^2`. Since all networks have only a single output, the output properties consist of a randomly generated real number and a randomly generated inequality direction. Random output samples from the network are used to roughly ensure that the real number property has an equal likelihood of being within the output range of the NN and being outside of it (either above or below all NN outputs on the input constraint set). The inequality direction is generated independently and with each direction having an equal probability. This scheme biases the benchmark towards verification problems for which counterexamples exist.

### --- List of all tllverifybench_2023 [fullycon_net] networks (From :<a href = 'https://github.com/ChristopherBrix/vnncomp2024_benchmarks'> vnncomp2024_benchmarks </a>)---

#### tllBench_n=2_N=M=16_m=1_instance_1_0.onnx 
	Number of parameters: 267307 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=16_m=1_instance_1_1.onnx 
	Number of parameters: 267307 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=16_m=1_instance_1_2.onnx 
	Number of parameters: 267307 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=16_m=1_instance_1_3.onnx 
	Number of parameters: 267307 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=24_m=1_instance_2_0.onnx 
	Number of parameters: 1355164 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=24_m=1_instance_2_1.onnx 
	Number of parameters: 1355164 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=24_m=1_instance_2_2.onnx 
	Number of parameters: 1355164 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=24_m=1_instance_2_3.onnx 
	Number of parameters: 1355164 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=32_m=1_instance_3_0.onnx 
	Number of parameters: 4231259 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=32_m=1_instance_3_1.onnx 
	Number of parameters: 4231259 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=32_m=1_instance_3_2.onnx 
	Number of parameters: 4231259 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=32_m=1_instance_3_3.onnx 
	Number of parameters: 4231259 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=40_m=1_instance_4_0.onnx 
	Number of parameters: 10394833 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=40_m=1_instance_4_1.onnx 
	Number of parameters: 10394833 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=40_m=1_instance_4_2.onnx 
	Number of parameters: 10394833 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=40_m=1_instance_4_3.onnx 
	Number of parameters: 10394833 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=48_m=1_instance_5_0.onnx 
	Number of parameters: 21400348 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=48_m=1_instance_5_1.onnx 
	Number of parameters: 21400348 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=48_m=1_instance_5_2.onnx 
	Number of parameters: 21400348 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=48_m=1_instance_5_3.onnx 
	Number of parameters: 21400348 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=56_m=1_instance_6_0.onnx 
	Number of parameters: 39665760 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=56_m=1_instance_6_1.onnx 
	Number of parameters: 39665760 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=56_m=1_instance_6_2.onnx 
	Number of parameters: 39665760 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=56_m=1_instance_6_3.onnx 
	Number of parameters: 39665760 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=64_m=1_instance_7_0.onnx 
	Number of parameters: 67387579 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=64_m=1_instance_7_1.onnx 
	Number of parameters: 67387579 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=64_m=1_instance_7_2.onnx 
	Number of parameters: 67387579 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=64_m=1_instance_7_3.onnx 
	Number of parameters: 67387579 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=8_m=1_instance_0_0.onnx 
	Number of parameters: 17171 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=8_m=1_instance_0_1.onnx 
	Number of parameters: 17171 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=8_m=1_instance_0_2.onnx 
	Number of parameters: 17171 
	Node types: ['Relu' 'Add' 'MatMul']

#### tllBench_n=2_N=M=8_m=1_instance_0_3.onnx 
	Number of parameters: 17171 
	Node types: ['Relu' 'Add' 'MatMul']

