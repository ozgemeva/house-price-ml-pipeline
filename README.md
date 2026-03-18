# House Price ML Pipeline
Production-style machine learning pipeline built from scratch using Python.

## Project Overview
This project implements an end-to-end machine learning workflow for house price prediction, including:

- Modular data loading
- Exploratory data analysis (EDA)
- Target skew analysis
- Feature engineering (log transformation)
- Config-driven pipeline structure

The goal is to demonstrate clean project architecture and reproducible ML workflow design.

## Project Structure
house-price-ml-pipeline/
│
├── config/
├── src/
│ ├── data_loader.py
│ ├── eda.py
│ ├── feature_engineering.py
│ ├── config_loader.py
  ├── data_cleaner.py
│
├── main.py
├── requirements.txt
└── .gitignore

## Configuration
All configurable parameters are managed via centralized configuration to avoid hard-coded values.
Examples:
- Target variable
- Histogram bins
- Model test size
- Random seed

## EDA Approach
- Target variable: `SalePrice`
- Checked missing values and categorized them by percentage
- Detected duplicate rows and cleaned dataset
- Applied log transformation to reduce right skewness
- Compared original vs transformed target distribution
  
## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib

## Future Improvements
- Regression model training
- RMSE evaluation
- Cross-validation
- Model comparison

## Author
Ozge Meva Yilmaz
