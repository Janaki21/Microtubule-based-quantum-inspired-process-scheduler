Title: Microtubules Inspired Quantum Adaptive Scheduling Algorithm 

 

Overview 

This algorithm introduces a novel CPU scheduling algorithm inspired by biological microtubules and quantum principles. Unlike classical deterministic scheduling methods like First Come First Serve (FCFS), Shortest Job First (SJF), Round Robin or Priority Scheduling, our approach leverages probabilistic task selection, dynamic instability and fluctuation driven fairness throughout the scheduling process. The algorithm mimics microtubule dynamics flowthroughs, where tasks behave like "cargo" moving dynamically, while also incorporating a quantum like superposition of choices that prevents rigid task ordering. The goal is to achieve balanced CPU utilization, fairness and adaptability in dynamic environments. 

 

Inspiration: 
	Microtubules inside biological cells transport proteins and molecules through random yet highly efficient processes. Similarly in CPU scheduling it needs to balance priorities while avoiding collision. We also draw inspiration from quantum computing concepts such as superposition and probabilistic collapse. In our system all these tasks temporarily exist in multiple possible scheduling states, and the CPU probabilistically selects one among them which is weighted by its priority. This fusion creates a scheduling system that is both adaptive and fair. 

 

Features of the Scheduler: 

Probabilistic task selection instead of deterministic queue ordering. 

Dynamic instability where priorities fluctuate randomly to mimic microtubule’s instability. 

Fairness over time where no single task controls the CPU cycles. 

Visual probability evolution, showing how task selection likelihood changes throughout dynamically. 

Scalability adapts when works with multiple tasks and adjusts in real time. 

 

System Design : 
 Step 1: Initialize a set of tasks, each with a priority value. Higher the priority indicates urgency but does not guarantee the selection.       
 Step 2: Convert task priorities into probability weights which will ensure the fact that a higher priority task have a greater chance of being selected but still allows lower priority task to occasionally win CPU cycles. 
 Step 3: At each scheduling step, select one task randomly according to these probabilities. 
 Step 4: Introduce fluctuation which is a random scaling factor between 0.8 and 1.2 to simulate microtubule dynamic instability. This means priorities are never static, instead they continuously shift by forcing adaptability. 
 Step 5: Update probabilities and repeat the complete process. 
 Step 6: Record scheduling history and visualize task frequency and probability evolution. 

Code Explanation: 

 Code Block 1: Demonstrates a small set of tasks being scheduled probabilistically with random fluctuations which will produces a histogram of task frequency. 
 
 Code Block 2: Extends the system by simulating 20 processes and tracking how probabilities work and evolve over time. They produce line plots showing how each tasks probability changes with each scheduling step. 

 Code Block 3:  The scheduler’s main execution loop runs while each process is assigned a probability weight based on burst time and priority, and one process is selected using weighted random sampling. The chosen process executes for one unit, reducing its burst time, while probabilities are recalculated so chances shift dynamically. This prevents starvation and adapts as processes evolve. Unlike classical schedulers like Round Robin, Priority, which follow fixed rules, this loop introduces a quantum like element selection is probabilistic but still fair and guided. It is the core mechanism that makes the scheduler both adaptive and balanced.  

 

 


 

Differences from Classical Scheduling: 
 Our proposed scheduling algorithm introduces a fundamentally different approach compared to traditional CPU scheduling techniques. In classical scheduling methods such as First Come First Serve, Shortest Job First, Round Robin or Priority Scheduling, processes are queued and executed based on static or deterministic rules. These methods follow rigid structures that can lead to inefficiencies when process arrival times, burst durations, or priorities fluctuate dynamically throughout the operation. For instance, Round Robin relies on a fixed quantum state which if becomes too large, behaves like FCFS and if too small, increases context switching overhead. Similarly, Priority Scheduling suffers from starvation issues and Shortest Job First cannot adapt effectively  

in real time scenarios. All these limitations arise because the classical models lack adaptive and probabilistic mechanisms to distribute CPU time more flexibly. 

Our quantum inspired process scheduling model addresses these limitations by introducing a probabilistic time allocation mechanism which is inspired from the concept of superposition in quantum theory. Instead of assigning fixed slots or strict ordering, each process is given a dynamic execution probability based on its burst time and priority. This creates a state called “superposition queue" where multiple processes exist simultaneously with varying similarities of selection. The scheduler then samples processes according to these probabilities, allowing fairer and more balanced distribution of CPU cycles. Such an approach adapts better to changing workloads, reduces starvation and ensures that both short and long processes receive execution opportunities proportionally. The probabilistic selection mirrors how quantum systems collapse into specific states and thus providing flexibility without chaos. 

Compared to deterministic scheduling, this model demonstrates greater adaptability in handling diverse workloads. For example, in heavy multitasking environments, it ensures that small tasks are not indefinitely delayed while long processes still make steady progress. The inclusion of dynamic probability adjustment allows the scheduler to continuously rebalance CPU allocation without relying on rigid rules. This results in improved average waiting time, reduced turnaround variance and a more equitable process execution pattern throughout. By combining mathematical modeling with concepts inspired by quantum mechanics, our approach introduces a new paradigm that bridges classical scheduling’s simplicity with the adaptability required in modern, high concurrency systems. 
 

Visualizations and Results: 
 	*The algorithm generates two key visual outputs: 
	*Task Selection Frequency Histogram which shows how many times each task was scheduled over multiple iterations. 
	*Probability Evolution Plot which shows how each task’s probability fluctuates dynamically over time, demonstrating fairness and instability. 

 

Applications & Future Scope: 
	*Operating system CPU scheduling for adaptive environments. 
 	*Real time embedded systems where fairness is critical. 
  	*Cloud computing load balancing. 
   	*Bio inspired AI systems. 
	*Extension towards quantum-inspired distributed schedulers. 



 
[Microtubule inspired process scheduling README file.pdf](https://github.com/user-attachments/files/22055933/Microtubule.inspired.process.scheduling.README.file.pdf)

 For represetation of the complete prototye outputs please refer the document attached above

 

 

 

 
