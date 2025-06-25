import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from datetime import timedelta


# Load the CSV file containing natural gas prices
data = pd.read_csv("nat_gas.csv")
data["Date"] = pd.to_datetime(data["Date"])
data.set_index("Date", inplace=True)


# Visualize the data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data["Price"], label="Historical Prices", marker="o")
plt.title("Natural Gas Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()


# Interpolation function to estimate price for any date
def estimate_price(date):
    date = pd.to_datetime(date)
    if date < data.index.min() or date > data.index.max():
        raise ValueError("Date out of range for interpolation.")
    interpolation = interp1d(
        data.index.values.astype(np.int64), data["Price"], kind="linear"
    )
    return interpolation(date.value)


# Extrapolation for one year into the future
def extrapolate_prices():
    last_date = data.index.max()
    future_dates = [last_date + timedelta(days=30 * i) for i in range(1, 13)]
    future_prices = []
    for i in range(1, 13):
        # Simple extrapolation using the average monthly change
        avg_monthly_change = data["Price"].diff().mean()
        future_prices.append(data["Price"].iloc[-1] + avg_monthly_change * i)
    return pd.DataFrame({"Date": future_dates, "Price": future_prices})


# Visualize extrapolated data
future_data = extrapolate_prices()
plt.figure(figsize=(10, 6))
plt.plot(data.index, data["Price"], label="Historical Prices", marker="o")
plt.plot(
    future_data["Date"],
    future_data["Price"],
    label="Extrapolated Prices",
    linestyle="--",
    marker="x",
)
plt.title("Natural Gas Prices with Extrapolation")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid()
plt.show()

# Example usage
input_date = "2023-06-15"
estimated_price = estimate_price(input_date)
print(f"Estimated price for {input_date}: ${estimated_price:.2f}")

# Save extrapolated data to a new CSV file
future_data.to_csv("extrapolated_natural_gas_prices.csv", index=False)
