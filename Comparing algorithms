# Microtubule inspired Process Scheduling (Prototype)
import random
import matplotlib.pyplot as plt
# Step 1: Define Processes
# This part defines a Process class with properties like ID, burst time, priority, etc.
# Then, 6 random processes are generated, each with a random burst time (3–10) and priority (1–5).
# These processes will be used as input for the scheduling algorithm.
class Process:
    def __init__(self, pid, burst_time, priority):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0

# Generate random processes for demo
processes = [Process(pid=i+1, burst_time=random.randint(3,10), priority=random.randint(1,5)) for i in range(6)]
# Step 2: Standard Algorithms
# FCFS: Runs processes in arrival order, each until completion.
# Round Robin: Runs processes in time slices (quantum) and cycles until all finish.
# Priority Scheduling: Runs processes based on priority (higher priority first).
def fcfs(processes):
    time = 0
    timeline = []
    for p in processes:
        time += p.burst_time
        p.completion_time = time
        timeline.append((p.pid, time))
    return timeline
def round_robin(processes, quantum=3):
    time = 0
    queue = processes[:]
    timeline = []
    while queue:
        p = queue.pop(0)
        if p.remaining_time > quantum:
            time += quantum
            p.remaining_time -= quantum
            queue.append(p)
        else:
            time += p.remaining_time
            p.remaining_time = 0
            p.completion_time = time
            timeline.append((p.pid, time))
    return timeline
def priority_scheduling(processes):
    time = 0
    timeline = []
    for p in sorted(processes, key=lambda x: x.priority):
        time += p.burst_time
        p.completion_time = time
        timeline.append((p.pid, time))
    return timeline
# Step 3: Microtubule-Inspired Scheduler
# Inspired by microtubule dynamics → probabilistic expansion/shrinkage
# Each process gets selected with a probability proportional to priority & inverse of burst time
# Microtubule inspired: process selection is probabilistic (priority ↑, burst time ↓)
# Assign weights = priority / burst_time, normalize to probabilities
# Randomly pick one process based on these probabilities
# Execute it for a small random quantum (1–3), simulating dynamic instability
# Update time, remaining burst, and mark completion when done
def microtubule_scheduler(processes, steps=30):
    time = 0
    timeline = []
    procs = processes[:]
    while any(p.remaining_time > 0 for p in procs):
        weights = [(p.priority / p.burst_time) if p.remaining_time > 0 else 0 for p in procs]
        total = sum(weights)
        if total == 0:
            break
        probs = [w/total for w in weights]
        chosen = random.choices(procs, weights=probs, k=1)[0]

        # Dynamic instability idea → execute small time quanta randomly (1-3)
        quanta = random.randint(1,3)
        exec_time = min(quanta, chosen.remaining_time)

        time += exec_time
        chosen.remaining_time -= exec_time

        if chosen.remaining_time == 0:
            chosen.completion_time = time
            timeline.append((chosen.pid, time))
    return timeline
# Step 4: Run & Compare
# Create fresh copies of processes for each algorithm (avoid shared state)
# Run FCFS, Round Robin, Priority, and Microtubule schedulers separately
# Collect their execution timelines for comparison
# Clone processes fresh for each run
procs1 = [Process(p.pid, p.burst_time, p.priority) for p in processes]
procs2 = [Process(p.pid, p.burst_time, p.priority) for p in processes]
procs3 = [Process(p.pid, p.burst_time, p.priority) for p in processes]
procs4 = [Process(p.pid, p.burst_time, p.priority) for p in processes]
fcfs_tl = fcfs(procs1)
rr_tl = round_robin(procs2)
prio_tl = priority_scheduling(procs3)
mt_tl = microtubule_scheduler(procs4)
# Step 5: Visualization
# Function to plot the execution timeline of each scheduling algorithm
# Draws horizontal bars for each process showing its run time
# Labels each bar with the process ID for clarity
# Adds title, X-axis (Time), and Y-axis (Processes) Generate timeline plots for
# FCFS, Round Robin, Priority, and Microtubule schedulers
def plot_timeline(timeline, title):
    plt.figure(figsize=(8,3))
    y = 1
    for pid, t in timeline:
        plt.barh(y, t, left=0)
        plt.text(t-0.5, y, f"P{pid}", color="white", ha="right")
        y += 1
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Process")
    plt.show()
plot_timeline(fcfs_tl, "FCFS Scheduling")
plot_timeline(rr_tl, "Round Robin Scheduling")
plot_timeline(prio_tl, "Priority Scheduling")
plot_timeline(mt_tl, "Microtubule-Inspired Scheduling")
# Metrics Calculation
# Calculates turnaround time (TAT), waiting time (WT), average TAT, average WT,
# and throughput for all processes.
# TAT = Completion time - Arrival time (arrival = 0 in this case).
# WT  = TAT - Burst time.
# Prints per-process metrics and overall averages.
def calculate_metrics(processes):
    n = len(processes)
    total_tat, total_wt = 0, 0
    metrics = []
    for p in processes:
        tat = p.completion_time  # turnaround = finish - arrival (arrival = 0 here)
        wt = tat - p.burst_time
        total_tat += tat
        total_wt += wt
        metrics.append((p.pid, tat, wt))
    avg_tat = total_tat/n
    avg_wt = total_wt/n
    throughput = n / max(p.completion_time for p in processes)

    print("\n=== Metrics ===")
    print("PID | TAT | WT")
    for pid, tat, wt in metrics:
        print(f"P{pid} | {tat} | {wt}")
    print(f"\nAvg Turn around Time: {avg_tat:.2f}, Avg Weighting Ttime: {avg_wt:.2f}, Throughput: {throughput:.2f}")
# Example: metrics for microtubule scheduler
procs_mt = [Process(p.pid, p.burst_time, p.priority) for p in processes]
microtubule_scheduler(procs_mt)
calculate_metrics(procs_mt)
