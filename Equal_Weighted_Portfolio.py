import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("nifty50_closing_prices.csv")

# First column is Date
df['Date'] = pd.to_datetime(df['Date'])

# Calculate normalized prices
normalized = df.iloc[:, 1:].div(df.iloc[:, 1:].iloc[0])  # start at 1

# Equal-weighted portfolio value
equal_weighted = normalized.mean(axis=1)

# Plot
plt.figure(figsize=(15, 8))
plt.plot(df['Date'], equal_weighted, label='Equal-Weighted Portfolio', color='blue')
plt.ylabel("Portfolio Value (Normalized)")
plt.title("Equal-Weighted Portfolio Performance - NIFTY50")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save chart
plt.savefig("equal_weighted_portfolio.png", dpi=300)
plt.close()
