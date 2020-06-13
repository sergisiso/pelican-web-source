Title: Publications
Date: 2010-12-02 10:20


<br>
<h2 class="fa fa-file-text fa-2x" style="display:inline"></h2><h2 style="display:inline;padding-left:20px;">Papers</h2>

**2019 - [Evaluating Auto-Vectorizing Compilers through Objective Withdrawal of Useful Information](https://dl.acm.org/citation.cfm?doid=3366460.3356842)** Sergi Siso, Wes Armour, Jeyan Thiyagalingam, *ACM Transactions on Architecture and Code Optimization (TACO) 16 (4), 40*

Abstract: "The need for compilers to generate highly vectorized code is at an all-time high with the increasing vectorization capabilities of modern processors. To this end, the information that compilers have at their disposal, either through code analysis or via user annotations, is instrumental for auto-vectorization, and hence for the overall performance. However, the information that is available to compilers at compile time and its accuracy varies greatly, as does the resulting performance of vectorizing compilers. Benchmarks like the Test Suite for Vectorizing Compilers (TSVC) have been developed to evaluate the vectorization capability of such compilers. The overarching approach of TSVC and similar benchmarks is to evaluate the compilers under the best possible scenario (i.e., assuming that compilers have access to all useful contextual information at compile time). Although this idealistic view is useful to observe the capability of compilers for auto-vectorization, it is not a true reflection of the conditions found in real-world applications.

In this article, we propose a novel method for evaluating the auto-vectorization capability of compilers. Instead of assuming that compilers have access to a wealth of information at compile time, we formulate a method to objectively supply or withdraw information that would otherwise aid the compiler in the auto-vectorization process. This method is orthogonal to the approach adopted by TSVC, and as such, it provides the means of assessing the capabilities of modern vectorizing compilers in a more detailed way."

**2016 - [Early Application Performance at the Hartree Centre with the OpenPOWER Architecture.](https://link.springer.com/chapter/10.1007/978-3-319-46079-6_13)** Mike Ashworth, Jianping Meng, Vedran Novakovic, Sergi Siso, *International Conference on High Performance Computing*

Abstract: "The Hartree Centre has been established as a UK focus for industrial
engagement. STFC has acquired a new IBM system based on the OpenPOWER
architecture, comprising 32 nodes with POWER8 CPUs and NVIDIA Kepler K80 GPUs.
We report early evaluation of the system using some real applications based on
the Lattice Boltzmann Method, Direct Numerical Simulation of Turbulence and
using FFTs. No optimisation has been carried out yet, but results are
encouraging with performance comparable or better on a per core basis to Intel
IvyBridge CPUs. Use of the GPUs for suitable algorithms such as Lattice
Boltzmann kernels and for FFTs provides further performance enhancements."

**2016 - [Code modernization of DL_MESO LBE to achieve good performance on the Intel Xeon Phi.](https://pdfs.semanticscholar.org/ea2c/9fa3fd73de1d97b3f2e4c981d3eedf6db5fe.pdf#page=15)** Sergi Siso, Luke Mason, Michael Seaton, *EMerging Technology (EMiT) Conference 2016*

Abstract: "The Lattice Boltzmann Equations of DL_MESO have been re-implemented using
a Two-Grid algorithm, threaded programming and vectorization in order to
effectively utilize novel highly parallel architectures such as the one offered
by the Intel Xeon Phi."

**2016 - [A new framework for variable resolution adaptive SPH with fully object-oriented SPHysics on emerging technology.](https://www.researchgate.net/publication/306056664_A_new_framework_for_variable_resolution_adaptive_SPH_with_fully_object-oriented_SPHysics_on_emerging_technology)** R Vacondio, SM Longshaw, S Siso, L Mason, BD Rogers, *Proc. 11th Smoothed Particle Hydrodynamics European Research Interest Community Conference (SPHERIC 2016)*

Abstract: "In this work the details of a novel highly-modular and parallel Smoothed
Particle Hydrodynamics (SPH) code are presented. The aim of this new code is to
introduce an Application Program Interface (API) developed using the
object-oriented programming approach available within modern Fortran language
, the motivation is to maximize the efficiency when variable resolution in SPH
is used. Hence, a novel type of data structure has been introduced, making an
extensive use of pointers and liked-list algorithms. In the paper details on
the different objects introduced and most relevant algorithm to create and
delete particles at minimal computational cost are reported. Moreover most
relevant algorithms are described and efficiency of the parallelization is
discussed considering different architectures, in particular a first attempt
has been made to run the code on Intel Xeon Phi."


<br>
<h2 class="fa fa-book fa-2x" style="display:inline"></h2><h2 style="display:inline;padding-left:20px;">Univerity thesis</h2>

**2014 - [Parallelisation of the Coupled Coherent States quantum dynamics simulation](https://static.ph.ed.ac.uk/dissertations/hpc-msc/2013-2014/Parallelisation%20of%20the%20Coupled%20Coherent%20States%20quantum%20dynamics%20simulation.pdf) (MSc in High Performance Computing dissertation)**, University of Edinburgh

Advisor: Andrew Turner <br>
Abstract: "The Coupled Coherent States is a quantum molecular dynamics method which solves the time-dependent Schrödinger equation in a basis of semi-classical trajectories in an attempt to avoid exponential scaling. This makes it able to simulate and study the time evolution of photochemical reactions.
This current project studies the performance of the Coupled Coherent States method and explores its potential parallelism. It proposes a parallel version of the simulation in order run the software faster and more accurately.
The simulation is divisible in two parts where different parallelisation approaches are used. The generation of the trajectories represents an embarrassingly parallel problem and can be solved with a task distribution solution. The propagation of the trajectories needs to solve a ODE, which represent a highly coupled problem. To solve it, the parallisation of the Runge-Kutta Cash-Karp method, the implementation of a parallel derivation routine and the use of parallel lineal algebra routines (ScaLAPACK) are proposed.
The final implementation achieves a speedup of x10 in the first part of the simulation, the generation of trajectories, and a x4.5 in the second part, the propagation of the trajectories, when they are run on 12 processors. Suggestions for further development of the parallel CCS code are also presented."

**2013 - [Simulating parallel systems using summarized application information](http://upcommons.upc.edu/pfc/handle/2099.1/18972) (MTI master thesis)**, Politechnic University of Catalonia

Advisor: Jesus Labarta <br>
Abstract: "Examine and analyse how we can use the summarized information of parallel applications generated by the Extrae instrumentation tool in order to model the behavior of the application in a feasible way to predict its impact and the performance in different architectures."

**2011 - [An electronic voting platform with elliptic curve cryptography](http://repositori.udl.cat/handle/10459.1/45765) (Bachelor final thesis)**, Univerity of Lleida

Advisor: J.M Miret <br>
Abstract: "This document is part of a wider project which presents an e-Voting platform based on elliptic curve cryptography. It uses an hybrid combination of two of the main e-Voting paradigms to guarantee privacy and security in the counting phase, these are precisely, the mixnets and the homomorphic protocols. This document is focused in the description of the system and the maths and programming needed to solve the homomorphic part of it. In later chapters, there is a comparison between a simple mixing system and our system proposal."

<br>
<h2 class="fa fa-pie-chart fa-2x" style="display:inline"></h2><h2 style="display:inline;padding-left:20px;">Presentations</h2>

**November 2015 - [DL MESO Lattice Boltzmann port to Intel Xeon Phi]()** *Supercomputing '15*, Austin

**November 2015 - [Benefits of Leveraging Software Defined Visualization]()** *Intel HPC Developer's Conference*, Austin

**October 2015 - [Benefits of Leveraging Software Defined Visualization](https://software.intel.com/en-us/ipcc/webinars)**, Intel PCC Webminar

**September 2015 - [DualSPHysics Performance on Intel Xeon Phi]({filename}/pdfs/DualSPHysics_UserGroup_XeonPhi.pdf)**, Presented at *UK SPH Symposium*, Daresbury & *DualSPHysics User Group*, Manchester

**July 2015 - [DL MESO Lattice Boltzman Data Layout]()**,  *Tutorial: The Road to Application Performance on Intel Xeon Phi, International Supercomputing Conference 15*, Frankfurt

**July 2015 - [Improving Vector Performance with Vector Advisor]({filename}/pdfs/hartree_simd_bof_v3.pdf)**, *SIMD BoF, International Supercomputing Conference 15*, Frankfurt

**December 2014 - [Coupled Coherent States]({filename}/pdfs/CCS_basic.pdf)**, *Quantum Dynamics Workshop* at University of Edinburgh, School of Chemistry


