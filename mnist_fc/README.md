# <a href="https://github.com/pat676/mnist_fc_vnncomp2022">mnist_fc_vnncomp2022</a>

**Proposed by The VeriNet team.**

**Motivation:** This benchmark contains fully connected networks with ReLU activation functions and varying depths.

**Networks:** The benchmark set consists of three fully connected classification networks with two, four, and six layers and ReLU nodes in each layer trained on the MNIST dataset. The networks were first presented in a benchmark in VNN-COMP.

### --- List of all mnist_fc [fullycon_net] networks (From :<a href = 'https://github.com/ChristopherBrix/vnncomp2022_benchmarks'> vnncomp2022_benchmarks </a>)---

#### mnist-net_256x2.onnx 
	Number of parameters: 269322 
	Node types: ['Gemm' 'Flatten' 'Relu']

#### mnist-net_256x4.onnx 
	Number of parameters: 400906 
	Node types: ['Gemm' 'Flatten' 'Relu']

#### mnist-net_256x6.onnx 
	Number of parameters: 532490 
	Node types: ['Gemm' 'Flatten' 'Relu']

