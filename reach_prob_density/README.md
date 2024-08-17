# <a href="https://github.com/stanleybak/reach_probability_benchmark2022">reach_probability_benchmark2022</a>
Benchmark for VNNCOMP 2022 related to reachability probability density networks

Meng, Yue, Dawei Sun, Zeng Qiu, Md Tawhid Bin Waez, and Chuchu Fan. "Learning Density Distribution of Reachable States for Autonomous Systems." In Conference on Robot Learning, pp. 124-136. PMLR, 2022.

## Vanderpol
vdp.onnx

rad 0.2 to 0.8
log_prob 0.15 to 0.3

trange = [0.0, 5.0]
init_box = np.array([[-2.5, 2.5], [-2.5, 2.5], trange], dtype=float)

## Robot
robot.onnx

rad = 0.0 to 0.3
log_prob between 0.05 and 0.3

 mat = np.array([[0, 1, 0, 0, 0], [0, -1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, -1, 0, 0], [-1, 0, 0, 0, 0]], dtype=float)
 
 
    rhs = np.array([rad, rad, rad, rad, -log_prob], dtype=float)
    spec = Specification(mat, rhs)
    
## GCAS

theta in range (tmax, 0)

with tmax between -1 and -0.5

varscale 

(-0.0100, 0.0100),

easy, *2 medium, *10 hard

### --- List of all reach_prob_density [fullycon_net] networks (From :<a href = 'https://github.com/ChristopherBrix/vnncomp2022_benchmarks'> vnncomp2022_benchmarks </a>)---

#### gcas.onnx 
	Number of parameters: 1998 
	Node types: ['Gemm' 'Relu']

#### robot.onnx 
	Number of parameters: 9029 
	Node types: ['Gemm' 'Relu']

#### vdp.onnx 
	Number of parameters: 1283 
	Node types: ['Gemm' 'Relu']

