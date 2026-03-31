import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from data_generator import generate_data
from model_utils import train_model, find_optimal_price, predict_demand, calculate_elasticity

data_path = "data/sales_data.csv"
results_path = "data/results.csv"

# Load or generate data
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    print("Loaded existing dataset")
else:
    df = generate_data()
    print("Generated new dataset")

X = df[['price']]
y = df['demand']

# Train model
model, poly = train_model(X, y)

# Find optimal price
opt_price, opt_demand, max_revenue = find_optimal_price(
    model, poly, df['price'].min(), df['price'].max()
)

# Elasticity
elasticity = calculate_elasticity(model, poly, opt_price)

# Print results (clean format)
print("\n========== RESULTS ==========")
print(f"Optimal Price       : {opt_price:.2f}")
print(f"Expected Demand     : {opt_demand:.2f}")
print(f"Maximum Revenue     : {max_revenue:.2f}")
print(f"Price Elasticity    : {elasticity:.2f}")
print("============================\n")

# Save results
results_df = pd.DataFrame({
    "Optimal Price": [opt_price],
    "Expected Demand": [opt_demand],
    "Maximum Revenue": [max_revenue],
    "Elasticity": [elasticity]
})

results_df.to_csv(results_path, index=False)
print("Results saved to", results_path)

# Visualization
prices = np.linspace(df['price'].min(), df['price'].max(), 200).reshape(-1, 1)
demand = predict_demand(model, poly, prices)
revenue = prices.flatten() * demand

plt.figure()
plt.scatter(df['price'], df['demand'], label="Data")
plt.plot(prices, demand, label="Demand Curve")
plt.xlabel("Price")
plt.ylabel("Demand")
plt.legend()
plt.title("Price vs Demand")
plt.show()

plt.figure()
plt.plot(prices, revenue)
plt.xlabel("Price")
plt.ylabel("Revenue")
plt.title("Revenue Optimization Curve")
plt.show()