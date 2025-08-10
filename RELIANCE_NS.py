import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read dataset
df = pd.read_csv("nifty50_closing_prices.csv")
df['Date'] = pd.to_datetime(df['Date'])

stock_name = 'RELIANCE.NS'
stock_prices = df[stock_name].values

# Convert into a matrix for heatmap (e.g., 6 rows x 4 cols for 24 data points)
rows, cols = 6, 4
price_matrix = stock_prices.reshape(rows, cols)

plt.figure(figsize=(8, 5))
sns.heatmap(price_matrix, annot=True, fmt=".2f", cmap="YlGnBu",
            cbar_kws={'label': 'Price'})
plt.title(f"{stock_name} Price Movement Heatmap")
plt.tight_layout()

# Save chart
plt.savefig(f"{stock_name.lower()}_heatmap.png", dpi=300)
plt.close()
