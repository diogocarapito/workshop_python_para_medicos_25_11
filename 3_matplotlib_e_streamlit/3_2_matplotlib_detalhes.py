import pandas as pd
import matplotlib.pyplot as plt

# Simulated health data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "New Patients": [120, 135, 160, 180, 210, 190],
    "Follow-ups": [80, 95, 110, 120, 140, 130]
}

df = pd.DataFrame(data)

# --- Explore the data ---
print("Data preview:")
print(df.head())

# --- Create a custom graph ---
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["New Patients"], label="New Patients", color="#1f77b4", linewidth=2, marker="o")
plt.plot(df["Month"], df["Follow-ups"], label="Follow-ups", color="#ff7f0e", linewidth=2, marker="s")

# Customize
plt.title("Monthly Consultations (Primary Care Center)")
plt.xlabel("Month")
plt.ylabel("Number of Visits")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(title="Type")
plt.tight_layout()

# Save the figure
plt.savefig("3_matplotlib_e_streamlit/monthly_consultations_matplotlib.png")