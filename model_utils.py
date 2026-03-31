from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(X, y, degree=2):
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    
    model = LinearRegression()
    model.fit(X_poly, y)
    
    return model, poly

def predict_demand(model, poly, prices):
    return model.predict(poly.transform(prices))

def find_optimal_price(model, poly, price_min, price_max):
    prices = np.linspace(price_min, price_max, 200).reshape(-1, 1)
    
    demand = predict_demand(model, poly, prices)
    revenue = prices.flatten() * demand
    
    idx = revenue.argmax()
    
    return prices[idx][0], demand[idx], revenue[idx]

def calculate_elasticity(model, poly, price):
    delta = 0.01
    
    p1 = price
    p2 = price + delta
    
    d1 = predict_demand(model, poly, np.array([[p1]]))[0]
    d2 = predict_demand(model, poly, np.array([[p2]]))[0]
    
    elasticity = ((d2 - d1) / d1) / (delta / p1)
    
    return elasticity
