import random
import numpy as np
import matplotlib.pyplot as plt

# Number of tasks (think of them as "cargo" moving along microtubules)
tasks = ["T1", "T2", "T3", "T4", "T5"]
task_priorities = [13, 6, 4, 2, 5]  # Higher = more urgent

# Microtubule-inspired probability weights
# Like "dynamic instability" – tasks can randomly get higher chance
probabilities = np.array(task_priorities) / sum(task_priorities)

# Simulate 20 scheduling decisions
schedule = []
for _ in range(20):
    chosen_task = np.random.choice(tasks, p=probabilities)
    schedule.append(chosen_task)
    # Introduce slight randomness (instability)
    fluctuation = np.random.uniform(0.8, 1.2, size=len(task_priorities))
    probabilities = np.array(task_priorities) * fluctuation
    probabilities = probabilities / sum(probabilities)
print("Probabilistic schedule:", schedule)
# Visualize distribution
plt.hist(schedule, bins=len(tasks), rwidth=0.8)
plt.title("Task Selection Frequency (Microtubule-inspired)")
plt.xlabel("Task")
plt.ylabel("Frequency")
plt.show()
# Track probability evolution
history = []
probabilities = np.array(task_priorities) / sum(task_priorities)
for _ in range(20):
    history.append(probabilities.copy())
    chosen_task = np.random.choice(tasks, p=probabilities)
    fluctuation = np.random.uniform(0.8, 1.2, size=len(task_priorities))
    probabilities = np.array(task_priorities) * fluctuation
    probabilities = probabilities / sum(probabilities)

history = np.array(history)

# Plot evolution of probabilities
plt.figure(figsize=(8,4))
for i, task in enumerate(tasks):
    plt.plot(history[:, i], label=task)
plt.title("Evolution of Task Selection Probabilities")
plt.xlabel("Step")
plt.ylabel("Probability")
plt.legend()
plt.show()

