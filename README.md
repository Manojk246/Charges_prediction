


💰 Medical Insurance Charges Predictor

This project predicts medical insurance charges based on demographic and lifestyle factors such as age, sex, BMI, children, smoking status, and region.
It includes machine learning models (Linear Regression, Random Forest, Gradient Boosting) and an interactive Streamlit app for real-time predictions.

Medical-insurance/
│── prediction.csv             
│── linear_regression.py        
│── random_forest.py            
│── gradient_boosting.py        
│── trained_model.sav           
│── app.py                      
│── README.md

📊 Dataset

The dataset prediction.csv contains the following columns:

Column	Description
age	Age of the person
sex	Gender (0 = Female, 1 = Male)
bmi	Body Mass Index
children	Number of children covered by health insurance
smoker	Smoking status (0 = No, 1 = Yes)
region	Region (0 = northeast, 1 = northwest, 2 = southeast, 3 = southwest)
charges	Medical charges billed by insurance

🧠 Models Implemented

Linear Regression → Baseline model for regression.

Random Forest Regressor → Ensemble model for higher accuracy.

Gradient Boosting Regressor → Boosted trees for performance.

Each model script:

Loads the dataset

Splits into train/test sets

Trains the model

Evaluates with R² score and RMSE

🚀 Future Improvements

Repo link : https://github.com/Manojk246/Charges_prediction.git
