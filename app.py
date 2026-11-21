import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Load trained pipeline
model = joblib.load(
    "models/salary_prediction_pipeline.pkl"
)

st.title("AI Job Salary Prediction")
st.write("Predict job salary based on job details")

# User inputs
job_title = st.selectbox(
    "Job Title",
    ["Data Scientist", "Data Analyst",
     "Data Engineer", "ML Engineer"]
)

experience_level = st.selectbox(
    "Experience Level",
    ["EN", "MI", "SE", "EX"]
)

employment_type = st.selectbox(
    "Employment Type",
    ["Full-time", "Part-time",
     "Contract", "Freelance"]
)

company_location = st.text_input(
    "Company Location", "United States"
)

company_size = st.selectbox(
    "Company Size",
    ["Small", "Medium", "Large"]
)

company_name = st.text_input("Company Name")

employee_residence = st.text_input(
    "Employee Residence"
)

education_required = st.selectbox(
    "Education Required",
    ["Bachelor's", "Master's", "PhD", "Other"]
)

years_experience = st.number_input(
    "Years of Experience", min_value=0, max_value=50
)

required_skills = st.text_input(
    "Required Skills", "Python, SQL, Machine Learning"
)

job_description_length = st.number_input(
    "Job Description Length", min_value=0
)

industry = st.text_input("Industry", "Technology")

remote_ratio = st.selectbox(
    "Remote Ratio", [0, 50, 100]
)

posting_date = st.date_input("Posting Date")

application_deadline = st.date_input(
    "Application Deadline"
)

benefits_score = st.number_input(
    "Benefits Score", min_value=0.0
)

salary_currency = st.selectbox(
    "Salary Currency", ["USD", "EUR", "GBP", "INR"]
)

# Prediction button
if st.button("Predict Salary"):

    input_data = pd.DataFrame([{
        "job_title": job_title,
        "experience_level": experience_level,
        "employment_type": employment_type,
        "company_location": company_location,
        "company_size": company_size,
        "company_name": company_name,
        "employee_residence": employee_residence,
        "education_required": education_required,
        "years_experience": years_experience,
        "required_skills": required_skills,
        "job_description_length": job_description_length,
        "industry": industry,
        "remote_ratio": remote_ratio,
        "posting_date": str(posting_date),
        "application_deadline": str(application_deadline),
        "benefits_score": benefits_score,
        "salary_currency": salary_currency
    }])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Salary: ${prediction[0]:,.2f}"
    )
    # Load trained pipeline
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "salary_prediction_pipeline.pkl"

model = joblib.load(MODEL_PATH)