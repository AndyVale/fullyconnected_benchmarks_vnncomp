# Benchmark for VNNCOMP 2024: Verify1s

We propose a benchmark for the [VNNCOMP 2024](https://sites.google.com/view/vnn2024) that focuses on verification time. Often, the verification of neural networks is slow; in some cases, the verification can take multiple days, which is often hard to justify. To encourage the fast verification of neural networks, our benchmark focuses on the verification time by setting a small timeout (1s).

The benchmark consists of one ReLU-neural network architecture (7x250 + ReLU), which was trained on three datasets, i.e., MNIST, SVHN, and CIFAR10, using three different training methods, i.e., standard (point), interval-bound propagation, and set-based. 
Both interval-bound propagation and set-based training are training methods that improve the robustness of the trained neural network.
The neural networks are taken from the first evaluation run of [1]; please refer to [1] for the training details.

## References
[1] Koller, Lukas, Tobias Ladner, and Matthias Althoff. "Set-Based Training for Neural Network Verification." [arXiv preprint arXiv:2401.14961](https://arxiv.org/abs/2401.14961) (2024).


### --- List of all cora [fullycon_net] networks (From :<a href = 'https://github.com/ChristopherBrix/vnncomp2024_benchmarks'> vnncomp2024_benchmarks </a>)---

#### cifar10-point.onnx 
	Number of parameters: 1147262 
	Node types: ['MatMul' 'Mul' 'Relu' 'Add']

#### cifar10-set.onnx 
	Number of parameters: 1147262 
	Node types: ['MatMul' 'Mul' 'Relu' 'Add']

#### cifar10-trades.onnx 
	Number of parameters: 1147262 
	Node types: ['MatMul' 'Mul' 'Relu' 'Add']

#### mnist-point.onnx 
	Number of parameters: 575260 
	Node types: ['Relu' 'Add' 'MatMul']

#### mnist-set.onnx 
	Number of parameters: 575260 
	Node types: ['Relu' 'Add' 'MatMul']

#### mnist-trades.onnx 
	Number of parameters: 575260 
	Node types: ['Relu' 'Add' 'MatMul']

#### svhn-point.onnx 
	Number of parameters: 1147262 
	Node types: ['MatMul' 'Mul' 'Relu' 'Add']

#### svhn-set.onnx 
	Number of parameters: 1147262 
	Node types: ['MatMul' 'Mul' 'Relu' 'Add']

#### svhn-trades.onnx 
	Number of parameters: 1147262 
	Node types: ['MatMul' 'Mul' 'Relu' 'Add']

