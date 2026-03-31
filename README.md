# Fundamentals-of-AI-and-ML-Evaluated-Course-Project
# Smart Price Optimization System

A Machine Learning project that predicts demand based on product price and determines the optimal price to maximize revenue.

---

## Overview

Pricing is a critical factor in business success. Setting the right price can significantly impact demand and revenue.

This project builds a data-driven price optimization system using Machine Learning and economic principles.

The system:
- Models the relationship between price and demand
- Predicts demand for different price levels
- Calculates revenue
- Finds the optimal price that maximizes revenue
- Computes price elasticity to measure sensitivity

---

## Features

- Synthetic data generation with realistic demand behavior
- Polynomial Regression model
- Revenue optimization
- Price elasticity calculation
- CSV data storage
- Data visualization (Demand and Revenue curves)

---

## Concepts Used

- Machine Learning (Regression)
- Polynomial Feature Transformation
- Revenue Optimization
- Price Elasticity (Economics)
- Data Visualization

---

## Project Structure

price-optimization/
│── data/
│   ├── sales_data.csv
│   └── results.csv
│
│── data_generator.py
│── model_utils.py
│── main.py
│
│── requirements.txt
│── README.md

---

## How to Run

python main.py

---

## Output

The program displays:

- Optimal Price  
- Expected Demand  
- Maximum Revenue  
- Price Elasticity  

Example:

========== RESULTS ==========
Optimal Price       : 42.75  
Expected Demand     : 118.40  
Maximum Revenue     : 5061.30  
Price Elasticity    : -1.25  
============================

---

## Data Files

- sales_data.csv: Generated dataset  
- results.csv: Final computed results  

---

## Visualizations

The system generates:

- Price vs Demand graph  
- Price vs Revenue graph  

These graphs help in understanding how pricing affects demand and revenue.

---

## How It Works

1. Generate synthetic price-demand data  
2. Train a polynomial regression model  
3. Predict demand across a range of prices  
4. Compute revenue for each price  
5. Select the price that maximizes revenue  
6. Calculate price elasticity  

---

## Future Improvements

- Use real-world datasets  
- Add multiple products  
- Include competitor pricing  
- Build a web interface using Streamlit  
- Use advanced models such as Random Forest or XGBoost  

