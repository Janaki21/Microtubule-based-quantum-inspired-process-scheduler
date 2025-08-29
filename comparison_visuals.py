import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Example processes (burst_time, priority)
processes = [
    {"id": "P1", "burst": 7, "priority": 3},
    {"id": "P2", "burst": 4, "priority": 2},
    {"id": "P3", "burst": 9, "priority": 1},
    {"id": "P4", "burst": 5, "priority": 4},
]
# Define weight function (burst time + priority inspired by microtubule dynamics)
def compute_weight(proc, alpha=0.5, beta=0.5):
    return alpha * (1/proc["burst"]) + beta * proc["priority"]

# Compute probabilities
weights = np.array([compute_weight(p) for p in processes])
probabilities = weights / np.sum(weights)

# Simulate scheduling decisions (probabilistic allocation)
schedule = np.random.choice(
    [p["id"] for p in processes],
    size=20,  # 20 time slots
    p=probabilities
)

print("Allocation Probabilities:", dict(zip([p["id"] for p in processes], probabilities)))
print("Simulated Schedule:", schedule)

# Visualization of probabilities
plt.bar([p["id"] for p in processes], probabilities)
plt.title("Probabilistic Allocation (Microtubule-inspired)")
plt.ylabel("Probability")
plt.show()

# metrics for demo (will be replaced with actual calc later)
metrics = {
    "FCFS": {"Avg Waiting Time": 4.2, "Avg Turnaround Time": 9.3},
    "SJF": {"Avg Waiting Time": 3.1, "Avg Turnaround Time": 7.8},
    "Round Robin": {"Avg Waiting Time": 5.0, "Avg Turnaround Time": 10.1},
    "Priority": {"Avg Waiting Time": 4.5, "Avg Turnaround Time": 8.7},
    "Microtubule-Inspired": {"Avg Waiting Time": 3.8, "Avg Turnaround Time": 8.2},
}
# Convert to DataFrame
df = pd.DataFrame(metrics).T
print(df)
# Plot comparison
df.plot(kind="bar", figsize=(10,6))
plt.title("Comparison of Scheduling Algorithms")
plt.ylabel("Time Units")
plt.xticks(rotation=30)
plt.legend(title="Metrics")
plt.show()
