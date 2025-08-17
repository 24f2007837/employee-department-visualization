import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io, base64

# Synthetic dataset creation (replace with your own CSV if available)
np.random.seed(7)
departments = ["Marketing", "Sales", "Engineering", "HR", "Finance", "Support"]
regions = ["North", "South", "East", "West"]
n = 100

df = pd.DataFrame({
    "EmployeeID": range(1, n+1),
    "Department": np.random.choice(departments, size=n, p=[0.22, 0.2, 0.25, 0.1, 0.13, 0.1]),
    "Region": np.random.choice(regions, size=n),
    "PerformanceScore": np.random.normal(3.4, 0.6, size=n).clip(1.0, 5.0).round(2)
})

# Save CSV for reference (optional)
df.to_csv("employees.csv", index=False)

# Calculate Marketing frequency
marketing_count = int((df["Department"] == "Marketing").sum())
print("Marketing department frequency:", marketing_count)

# Plot histogram of departments (categorical count plot)
plt.figure(figsize=(8, 8))  # 8in * 64dpi = 512px
ax = df["Department"].value_counts().sort_values(ascending=False).plot(kind="bar")
ax.set_title("Employee Count by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Count")
plt.tight_layout()

# Save final image as exactly 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()