# House Price ML Pipeline
A production-style machine learning pipeline built from scratch using Python, focused on understanding how data quality impacts model performance.

## Project Motivation
Most beginners focus on building models.
In this project, I focused on something more important:
Understanding how data, features, and targets shape model behavior.
This project is not about achieving high accuracy.It is about building a solid foundation for reliable machine learning systems.

## Project Overview
This project implements an end-to-end machine learning workflow for house price prediction, including:

- Data loading with modular structure
- Exploratory Data Analysis (EDA)
- Missing data analysis and cleaning
- Duplicate detection and removal
- Target distribution analysis
- Log transformation to handle skewness
- Config-driven pipeline design

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
All parameters are centralized to ensure reproducibility:

- Target variable
- Histogram bins
- Train/test split
- Random seed

## Dataset
This project uses the "House Prices - Advanced Regression Techniques" dataset from Kaggle:
https://www.kaggle.com/datasets/rishitaverma02/house-prices-advanced-regression-techniques
The dataset contains detailed information about residential homes and is commonly used for regression problems.

## How to Run
pip install -r requirements.txt
python main.py

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
