import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("nifty50_closing_prices.csv")

# Ensure Date column is datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])
df.set_index('Date', inplace=True)

# Keep only numeric columns (stock prices)
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna(axis=1, how='all')  # Drop columns that are completely NaN

# Calculate daily returns
daily_returns = df.pct_change().dropna(how='all')

# If no returns exist, raise an error
if daily_returns.empty:
    raise ValueError("No price data found. Check your CSV format.")

# Calculate annualized return and risk
annual_returns = daily_returns.mean() * 252
annual_risk = daily_returns.std() * np.sqrt(252)

risk_return_df = pd.DataFrame({
    'Annual Return': annual_returns,
    'Annual Risk': annual_risk
}).dropna()

# Plot Risk vs Return
plt.figure(figsize=(18, 10))
plt.scatter(risk_return_df['Annual Risk'], risk_return_df['Annual Return'], color='blue')

# Annotate stock names
for stock in risk_return_df.index:
    plt.annotate(stock, (risk_return_df['Annual Risk'][stock], risk_return_df['Annual Return'][stock]),
                 textcoords="offset points", xytext=(5, 5), ha='left')

plt.xlabel('Annualized Risk (Volatility)')
plt.ylabel('Annualized Return')
plt.title('Risk vs Return for NIFTY50 Stocks')
plt.grid(True)
plt.savefig("risk_return_analysis.png", dpi=300, bbox_inches='tight')
plt.show()
