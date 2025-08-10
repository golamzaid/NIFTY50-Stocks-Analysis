import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("nifty50_closing_prices.csv")

# Calculate percentage change for each stock
returns = (df.iloc[-1, 1:] - df.iloc[0, 1:]) / df.iloc[0, 1:] * 100

# Top 5 gainers & losers
top_gainers = returns.sort_values(ascending=False).head(5)
top_losers = returns.sort_values().head(5)

# Plot
plt.figure(figsize=(10, 6))
plt.bar(top_gainers.index, top_gainers.values, color='green', label='Top Gainers')
plt.bar(top_losers.index, top_losers.values, color='red', label='Top Losers')
plt.ylabel("Percentage Change (%)")
plt.title("Top 5 Gainers & Losers - NIFTY50")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("gainers_losers.png", dpi=300)
plt.close()
