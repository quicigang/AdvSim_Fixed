import pandas as pd
import matplotlib.pyplot as plt

# List of CSV files with their respective scenario names
files = {
    "Data/All_Scenario_Policy/BAU - policy - curved utility function.csv": "BAU - Curved Utility",
    "Data/All_Scenario_Policy/BAU - policy - piecewise binary function.csv": "BAU - Piecewise Binary",
    #"Data/All_Scenario_Policy/Paris agreement - policy - curved utility function.csv": "Paris Agreement - Curved Utility",
    #"Data/All_Scenario_Policy/Paris agreement - policy - piecewise binary function.csv": "Paris Agreement - Piecewise Binary",
    #"Data/All_Scenario_Policy/Slow energy transition - policy - curved utility function.csv": "Slow Energy Transition - Curved Utility",
    #"Data/All_Scenario_Policy/Slow energy transition - policy - piecewise binary function.csv": "Slow Energy Transition - Piecewise Binary",
    #"Data/All_Scenario_Policy/Stated Policy Scenario - policy - curved utility function.csv": "Stated Policy Scenario - Curved Utility",
    #"Data/All_Scenario_Policy/Stated Policy Scenario - policy - piecewise binary function.csv": "Stated Policy Scenario - Piecewise Binary"
}

# Dictionary to store scenario data
scenario_data = {}

# Loop through each file and extract the Production Capacity [EU] data
for file, scenario in files.items():
    try:
        df = pd.read_csv(file)

        # Find the row with "Production capacity (tonne/year)"[EU]
        row = df[df.iloc[:, 0].str.contains("Production capacity.*\\[China\\]", na=False)]

        # Extract year columns and values
        years = df.columns[2:].astype(float)
        values = row.iloc[0, 2:].values.flatten().astype(float)

        scenario_data[scenario] = (years, values)
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Define a list of colors
colors = [
    "#001F3F", "#0074D9", "#7FDBFF", "#39CCCC",
    "#3D9970", "#2ECC40", "#FFDC00", "#FF851B"
]

# Plot each scenario
for (scenario, (years, values)), color in zip(scenario_data.items(), colors):
    ax.plot(years, values, label=scenario, color=color, linewidth=1.5)

# Set limits and styling
if scenario_data:
    ax.set_xlim(2020, 2050)
    ax.set_ylim(min(min(v[1]) for v in scenario_data.values()) * 0.96,
                max(max(v[1]) for v in scenario_data.values()) * 1.08)

ax.set_title("Nickel Production Capacity [EU] Across Scenarios (tonne/year)", fontsize=14, pad=10)
ax.set_xticks(range(2020, 2051, 5))
ax.grid(axis='y', linestyle="--", linewidth=0.5, alpha=0.7)

# Clean up spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_linewidth(1)

# Labels
ax.set_xlabel("")
ax.set_ylabel("")

# Add legend
ax.legend(loc="upper left", fontsize=9)

# Show plot
plt.show()
