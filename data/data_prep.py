import pandas as pd
import numpy as np

data = pd.read_csv("data/hba1c.csv")

data["trimeste"] = "2025_T3"

trimesters = [
    "2025_T3",
    "2025_T2",
    "2025_T1",
    "2024_T4",
    "2024_T3",
    "2024_T2",
    "2024_T1",
]


# Generate a random float with a Gaussian distribution
mean = 0.1  # Mean of the distribution
std_dev = 0.2  # Standard deviation of the distribution
lower_bound = -2  # Minimum value
upper_bound = 3  # Maximum value

for trimester in trimesters:

    if trimester == trimesters[0]:
        continue
    previous_trimester = trimesters[trimesters.index(trimester) - 1]

    data_previous = data[data["trimeste"] == previous_trimester].copy()

    data_previous["trimeste"] = trimester

    for each in data_previous.index:

        if np.random.rand() < 0.5:  # 50% chance
            rand_coeff = np.clip(
                np.random.normal(loc=mean, scale=std_dev), lower_bound, upper_bound
            )

            data_previous.loc[each, "Hemoglobina_A1c"] = round(
                data_previous.loc[each, "Hemoglobina_A1c"] + rand_coeff, 2
            )

    data = pd.concat([data, data_previous], ignore_index=True)

# drop na rows with no hba1c value
data = data.dropna(subset=["Hemoglobina_A1c"])

data.to_csv("data/hba1c_por_trimestres.csv", index=False)
