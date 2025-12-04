import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. Define ChipBlock Class
# -------------------------------------------------------------
class ChipBlock:
    def __init__(self, name, delay, dyn_power, leakage, area):
        self.name = name
        self.delay = delay
        self.dyn_power = dyn_power
        self.leakage = leakage
        self.area = area

    # Performance Index (lower is better) — Simplified formula
    def performance_index(self):
        return self.delay * (self.dyn_power + self.leakage)

    # Power Density = Total Power / Area
    def power_density(self):
        total_power = self.dyn_power + self.leakage
        return total_power / self.area

    # Timing Violation Check (threshold = 1.5 ns)
    def timing_violation(self, threshold=1.5):
        return self.delay > threshold


# -------------------------------------------------------------
# 2. Input VLSI Block Data
# -------------------------------------------------------------
raw_data = [
    ("ALU", 1.2, 35, 2.1, 500),
    ("RegisterFile", 1.8, 25, 1.5, 300),
    ("Decoder", 1.4, 15, 0.8, 200),
    ("DSP", 2.0, 50, 3.0, 600),
    ("Cache", 1.1, 20, 1.2, 450)
]

# -------------------------------------------------------------
# 3. Convert raw data into ChipBlock objects
# -------------------------------------------------------------
blocks = [ChipBlock(*item) for item in raw_data]

# -------------------------------------------------------------
# 4. Convert to Pandas DataFrame
# -------------------------------------------------------------
df = pd.DataFrame({
    "Name": [b.name for b in blocks],
    "Delay(ns)": [b.delay for b in blocks],
    "DynamicPower(mW)": [b.dyn_power for b in blocks],
    "Leakage(mW)": [b.leakage for b in blocks],
    "Area(um2)": [b.area for b in blocks],
    "PerformanceIndex": [b.performance_index() for b in blocks],
    "PowerDensity(mW/um2)": [b.power_density() for b in blocks],
    "TimingViolation": [b.timing_violation() for b in blocks]
})

print(df)

# -------------------------------------------------------------
# 5. NumPy Analysis
# -------------------------------------------------------------
mean_delay = np.mean(df["Delay(ns)"])
max_power_density = np.max(df["PowerDensity(mW/um2)"])

print("\nMean Delay:", mean_delay)
print("Max Power Density:", max_power_density)

# -------------------------------------------------------------
# 6. Identify worst block based on Performance Index
# -------------------------------------------------------------
worst_block = df.loc[df["PerformanceIndex"].idxmax()]
print("\nWorst Block Based on Performance Index:")
print(worst_block)

# -------------------------------------------------------------
# 7. Save reports (CSV + JSON)
# -------------------------------------------------------------
df.to_csv("vlsi_block_report.csv", index=False)
df.to_json("vlsi_block_report.json", orient="records", indent=4)

print("\nReports saved as vlsi_block_report.csv and vlsi_block_report.json")

# -------------------------------------------------------------
# 8. Generate Delay Bar Plot
# -------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Delay(ns)"])
plt.xlabel("Block Name")
plt.ylabel("Delay (ns)")
plt.title("Delay Comparison of VLSI Blocks")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("delay_plot.png")
plt.show()

print("Delay plot saved as delay_plot.png")
