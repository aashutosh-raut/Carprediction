# Carprediction
Car Prediction Software by Aashu


A machine learning project to predict the selling price of used cars based on features such as brand, mileage, engine capacity, fuel type, transmission, and more.

This repository contains data preprocessing, exploratory data analysis (EDA), feature engineering, model training, hyperparameter tuning, and evaluation of multiple regression models to find the most accurate predictor for car prices.

📂 Project Structure

Dataset: Cars.csv (8,128 records, 13 features)

Notebook / Scripts: Code for data preprocessing, visualization, training, and evaluation

Model File: car_prediction.model (trained Random Forest Regressor, pickled for reuse)

README: Project documentation

🔍 Dataset

The dataset consists of information on second-hand cars, including:

brand: Car brand (Maruti, Honda, Hyundai, etc.)

year: Year of manufacture

selling_price: Price of the car (target variable)

km_driven: Kilometers driven

fuel: Fuel type (Petrol/Diesel)

seller_type: Individual / Dealer

transmission: Manual / Automatic

owner: Number of previous owners

mileage, engine, max_power, seats: Technical specifications

After cleaning, final dataset had ~8,028 rows and 9 features.

⚙️ Data Preprocessing

Removed irrelevant values (LPG, CNG, Test Drive Cars)

Converted categorical features using Label Encoding

Cleaned mileage, engine, and power columns by extracting numeric values

Handled missing values with median imputation

Feature scaling using StandardScaler

Removed outliers (boxplot & IQR method)

Log transformation applied to target variable for better distribution

📊 Exploratory Data Analysis (EDA)

Distribution of owners, fuel types, transmissions, seats

Boxplots & scatterplots between mileage, engine, max_power, and price

Correlation heatmap to select relevant features

🤖 Models Used

The following models were trained and compared:

Linear Regression – R²: ~0.64

Support Vector Regression (SVR) – Struggled with scaling, poor results

KNeighbors Regressor (KNN) – Better than SVR, sensitive to outliers

Decision Tree Regressor – Captured non-linear patterns well

Random Forest Regressor – ⭐ Best performing model

🏆 Results

Best Model: Random Forest Regressor

Best Parameters:

{ "bootstrap": true, "max_depth": None, "n_estimators": 12 }


Performance:

R² Score: 0.916 (~92% variance explained)

MSE: 5.6 × 10¹⁰

🔑 Feature Importance

Top features influencing price prediction:

Max Power

Engine

Mileage

Km Driven

Brand

💾 Model Usage
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("car_prediction.model", "rb"))

# Example input: [brand, km_driven, fuel, seller_type, milage, engine, max_power, seats]
sample = np.array([[27.0, 120000, 0.0, 1.0, 21.14, 1498.0, 103.52, 5.0]])

# Predict price
predicted_price = model.predict(sample)
print("Predicted Car Price:", predicted_price)

📌 Future Improvements

Add more features (region, car condition, accident history, service records)

Explore deep learning regression models

Build a web interface for real-time car price predictions
