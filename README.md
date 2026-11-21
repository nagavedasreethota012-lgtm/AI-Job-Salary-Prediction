# AI Job Salary Prediction using Machine Learning

## 1. Project Overview

AI Job Salary Prediction is a Machine Learning project that predicts the estimated salary of professionals working in Artificial Intelligence and related fields based on various job-related factors.

The project uses historical job salary data to identify patterns and relationships between salary and factors such as experience level, employment type, job title, company location, employee residence, and remote work ratio.

An interactive web application is developed using Streamlit, allowing users to enter job-related information and receive an estimated salary prediction.

## 2. Problem Statement

The demand for Artificial Intelligence professionals is increasing rapidly across different industries.

However, predicting the appropriate salary for AI professionals can be challenging because salaries vary depending on experience, job role, company location, employment type, and other factors.

The objective of this project is to develop a Machine Learning model that predicts the estimated salary of AI professionals based on relevant job-related attributes.

## 3. Project Objectives

- Analyze AI job salary data.
- Understand the factors influencing AI salaries.
- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Identify important features affecting salaries.
- Train and evaluate Machine Learning models.
- Predict salaries based on user inputs.
- Build an interactive frontend using Streamlit.
- Deploy the application locally or on a cloud platform.
- Implement basic MLOps practices.

## 4. Dataset Description

The dataset contains information about salaries in Artificial Intelligence and related job roles.

Possible features include:

| Feature | Description |
|---|---|
| work_year | Year of salary record |
| experience_level | Employee experience level |
| employment_type | Type of employment |
| job_title | Employee job role |
| salary | Salary amount |
| salary_currency | Salary currency |
| salary_in_usd | Salary converted to USD |
| employee_residence | Employee's country |
| remote_ratio | Percentage of remote work |
| company_location | Company's country |
| company_size | Company size |

**Target Variable:** salary_in_usd

*Note: Confirm the actual column names against your dataset before implementation.*

## 5. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- MLflow
- Git and GitHub

## 6. Project Structure

```text
AI-Job-Salary-Prediction/
│
├── data/
│   └── ai_job_salary.csv
│
├── notebooks/
│   └── salary_analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── predict.py
│   └── experiment.py
│
├── models/
│   └── model.pkl
│
├── app/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 7. Project Workflow

### Step 1: Data Collection
Collected AI job salary data for analysis and model development.

### Step 2: Data Preprocessing
- Checked for missing values.
- Removed duplicate records where appropriate.
- Handled categorical variables.
- Converted data into suitable formats.
- Prepared features for Machine Learning.

### Step 3: Exploratory Data Analysis
- Analyzed salary distributions.
- Studied salary differences by experience level.
- Compared salaries across job titles.
- Analyzed salary variations by company location.
- Explored remote work and company size.

### Step 4: Feature Engineering
Selected relevant features for salary prediction and transformed categorical variables into numerical representations.

### Step 5: Model Training
Trained suitable regression algorithms, such as:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

### Step 6: Model Evaluation
Evaluated model performance using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Step 7: Model Saving
Saved the trained Machine Learning model using Joblib.

### Step 8: Frontend Development
Developed an interactive Streamlit application where users can enter job details and receive estimated salary predictions.

### Step 9: Deployment
Deployed the application locally or using a cloud platform.

## 8. Application Features

- User-friendly interface.
- Job-related input fields.
- Experience-level selection.
- Job title selection.
- Employment type selection.
- Company location selection.
- Remote work ratio selection.
- Predicted salary display.

## 9. Model Performance

| Evaluation Metric | Result |
|---|---|
| MAE | To be updated |
| MSE | To be updated |
| RMSE | To be updated |
| R² Score | To be updated |

The evaluation metrics will be updated after training and testing the final model.

## 10. MLOps Practices

### Version Control
Git and GitHub are used to maintain source code and track project changes.

### Experiment Tracking
MLflow is used to track:
- Model parameters
- Experiment runs
- Performance metrics
- Model artifacts

### Logging and Monitoring
Prediction logs are maintained to record model prediction activities and errors.

Model performance can be monitored by comparing predictions with actual salary values when available.

## 11. How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd AI-Job-Salary-Prediction
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app/app.py
```

### Step 5: Open in Browser

```text
http://localhost:8501
```

Enter the required job details and click the Predict button to view the estimated salary.

## 12. Expected Outcome

The project aims to develop a Machine Learning regression model that estimates AI job salaries based on relevant employment and company-related features.

The Streamlit application provides an accessible interface for users to explore salary predictions.

## 13. Future Enhancements

- Improve prediction accuracy.
- Include additional job market data.
- Explore advanced regression algorithms.
- Add interactive salary visualizations.
- Implement automated model retraining.
- Improve model monitoring.
- Deploy the application on cloud infrastructure.

## 14. Conclusion

AI Job Salary Prediction demonstrates the complete Machine Learning lifecycle, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, frontend development, deployment, and MLOps practices.

This project helps demonstrate how Machine Learning can be applied to analyze job market trends and estimate salaries for professionals in the Artificial Intelligence industry.

## 15. Author

**Name:** Thota NagaVedasree

**Project:** AI Job Salary Prediction

**GitHub:** https://github.com/nagavedasreethota012-lgtm/AI-Job-Salary-Prediction/tree/main

**LinkedIn:** www.linkedin.com/in/naga-vedasree-thota-056388279
