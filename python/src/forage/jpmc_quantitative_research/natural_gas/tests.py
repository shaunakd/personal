"""After asking around for the source of the existing data, you learn that the current process is to take a monthly snapshot of prices from a market data provider, which represents
the market price of natural gas delivered at the end of each calendar month. This data is available for roughly the next 18 months and is combined with historical prices in a time
series database. After gaining access, you are able to download the data in a CSV file.

You should use this monthly snapshot to produce a varying picture of the existing price data, as well as an extrapolation for an extra year, in case the client needs an indicative
price for a longer-term storage contract.

Download the monthly natural gas price data. Each point in the data set corresponds to the purchase price of natural gas at the end of a month, from 31st October 2020 to 30th
September 2024. Analyze the data to estimate the purchase price of gas at any date in the past and extrapolate it for one year into the future. Your code should take a date as
input and return a price estimate. Try to visualize the data to find patterns and consider what factors might cause the price of natural gas to vary. This can include looking at
months of the year for seasonal trends that affect the prices, but market holidays, weekends, and bank holidays need not be accounted for.
"""

from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file containing natural gas prices
data = pd.read_csv("natural_gas_prices.csv")
data["Date"] = pd.to_datetime(data["Date"])
data.set_index("Date", inplace=True)

# Drop rows with missing values
data = data.dropna(subset=["Price"])

# Normalize date values to avoid large numbers
normalized_dates = (data.index - data.index.min()).days

# Fit a polynomial to the historical data.
# A higher-degree polynomial can capture more complex trends, but it may also lead to overfitting.
# I tried this with degree 70, which fits the historical data exceptionnally well, but the extrapolation becomes meaningless due to the volatility.
degree = 5
coefficients = np.polyfit(normalized_dates, data["Price"], deg=degree)
polynomial = np.poly1d(coefficients)


# Function to estimate price for any date
def estimate_price(date):
    """Estimate the price of natural gas for a given date using polynomial regression.

    Args:
        date (str or datetime): The date for which to estimate the price.

    Returns:
        float: The estimated price of natural gas.
    """
    date = pd.to_datetime(date)
    normalized_date = (date - data.index.min()).days
    return polynomial(normalized_date)


def extrapolate_future(data, polynomial, months=12):
    """Extrapolate natural gas prices for one year into the future.

    Args:
        data (pd.DataFrame): DataFrame containing the natural gas price data.
        polynomial (np.poly1d): Polynomial object for extrapolation.
        months (int): Number of months to extrapolate.

    Returns:
        pd.DataFrame: DataFrame containing extrapolated future prices.
    """
    future_dates = pd.date_range(
        start=data.index.max() + timedelta(days=1), periods=months, freq="M"
    )
    future_normalized_dates = (future_dates - data.index.min()).days
    future_prices = polynomial(future_normalized_dates)
    future_data = pd.DataFrame({"Date": future_dates, "Price": future_prices})
    return future_data


# Extrapolate future prices for one year
future_data = extrapolate_future(data, polynomial, months=12)

# Plot the extrapolated future prices
plt.figure(figsize=(10, 6))
plt.plot(data.index, data["Price"], label="Historical Prices", marker="o")
plt.plot(
    data.index,
    polynomial(normalized_dates),
    label="Polynomial Fit",
    color="red",
    linestyle="--",
)
plt.plot(
    future_data["Date"],
    future_data["Price"],
    label="Extrapolated Future Prices",
    color="green",
    marker="x",
    linestyle="--",
)
plt.title("Natural Gas Prices: Historical, Fit, and Extrapolated Future")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()

# Visualize the historical data and polynomial fit
plt.figure(figsize=(10, 6))
plt.plot(data.index, data["Price"], label="Historical Prices", marker="o")
plt.plot(
    data.index,
    polynomial(normalized_dates),
    label="Polynomial Fit",
    color="red",
    linestyle="--",
)
plt.title("Natural Gas Prices with Polynomial Fit")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()

# Example usage
input_date = "2023-06-15"
estimated_price = estimate_price(input_date)
print(f"Estimated price for {input_date}: ${estimated_price:.2f}")
