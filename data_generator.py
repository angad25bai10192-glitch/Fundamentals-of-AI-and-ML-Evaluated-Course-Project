import pandas as pd
import numpy as np
import os

def generate_data(n=100, save_path="data/sales_data.csv"):
    np.random.seed(42)
    
    price = np.linspace(10, 100, n)
    
    # Non-linear demand (more realistic)
    demand = 300 - 2.5*price + 0.02*(price**2) + np.random.normal(0, 10, n)
    
    df = pd.DataFrame({
        'price': price,
        'demand': demand
    })
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    
    print("Data saved to", save_path)
    return df