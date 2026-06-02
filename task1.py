import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population.csv", sep="\t")
df.columns = df.columns.str.strip().str.replace('"', '')

df['Most Recent Value (Thousands)'] = pd.to_numeric(
    df['Most Recent Value (Thousands)'],
    errors='coerce')
df = df.dropna(subset=['Most Recent Value (Thousands)'])

plt.figure(figsize=(12, 7))
plt.hist(df['Most Recent Value (Thousands)'], bins=10, color='lightblue', edgecolor='black', linewidth=1.2)
plt.title('Population Distribution Across Countries (2024)')
plt.xlabel('Population (Thousands)')
plt.ylabel('Number of Countries')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("population_histogram.png", dpi=300, bbox_inches='tight')
plt.show()
