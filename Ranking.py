import pandas as pd

# Load the dataset
df = pd.read_csv("nifty50_closing_prices.csv") 

# Calculate percentage change for each stock from first to last available period
pct_change = ((df.iloc[-1, 1:] - df.iloc[0, 1:]) / df.iloc[0, 1:]) * 100

# Create a ranking DataFrame
ranking_df = pd.DataFrame({
    'Stock': pct_change.index,
    'Percentage Change': pct_change.values
})

# Sort stocks by percentage change (descending)
ranking_df = ranking_df.sort_values(by='Percentage Change', ascending=False).reset_index(drop=True)

# Save the ranked list to CSV
ranking_df.to_csv("stock_ranking_by_pct_change.csv", index=False)

# Display top and bottom 5
print("Top 5 Stocks by % Change:")
print(ranking_df.head())

print("\nBottom 5 Stocks by % Change:")
print(ranking_df.tail())
