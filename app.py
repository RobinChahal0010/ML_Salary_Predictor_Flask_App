from flask import Flask, render_template, request
import joblib
import pandas as pd
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

app = Flask(__name__, static_folder="static", template_folder="templates")

# ---------------- Load Model ----------------
model = joblib.load("model/salary_model.pkl")

# ---------------- Ensure Folders ----------------
os.makedirs("static", exist_ok=True)
os.makedirs("static/reports", exist_ok=True)

# ---------------- Dataset Columns ----------------
categorical_cols = [
    "experience_level", "employment_type", "job_title",
    "employee_residence", "company_size", "company_location"
]
numeric_cols = ["work_year", "remote_ratio"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # ---------- INPUT ----------
    job_title = request.form.get("job_title", "Data Scientist")
    experience = request.form.get("experience", "MI")  # EN, MI, SE, EX
    employment_type = request.form.get("employment_type", "FT")
    location = request.form.get("location", "US")
    company_size = request.form.get("company_size", "M")
    remote_ratio = int(request.form.get("remote_ratio", 0) or 0)
    company_location = request.form.get("company_location", location)

    # Build input dataframe (matching dataset structure)
    input_data = pd.DataFrame([{
        "work_year": datetime.now().year,
        "experience_level": experience,
        "employment_type": employment_type,
        "job_title": job_title,
        "employee_residence": location,
        "remote_ratio": remote_ratio,
        "company_location": company_location,
        "company_size": company_size
    }])

    # Ensure all model features exist
    for col in model.feature_names_in_:
        if col not in input_data.columns:
            input_data[col] = "" if col in categorical_cols else 0

    input_data = input_data[model.feature_names_in_]

    # ---------- PREDICTION ----------
    salary = round(model.predict(input_data)[0], 2)

    # ---------- Dynamic Salary by Role ----------
    roles = ["Data Analyst", "Data Scientist", "Software Engineer", "ML Engineer"]
    role_predictions = []
    for r in roles:
        df_role = input_data.copy()
        df_role["job_title"] = r
        role_predictions.append(round(model.predict(df_role)[0], 2))

    # ---------- What-if Analysis (Experience vs Salary) ----------
    experience_levels = ["EN", "MI", "SE", "EX"]
    salary_vs_experience = []
    for exp in experience_levels:
        df_exp = input_data.copy()
        df_exp["experience_level"] = exp
        salary_vs_experience.append(round(model.predict(df_exp)[0], 2))

    # ---------- PDF REPORT ----------
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_path = f"static/reports/prediction_{timestamp}.pdf"

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "💰 Salary Prediction Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Job Title: {job_title}")
    c.drawString(50, height - 100, f"Experience Level: {experience}")
    c.drawString(50, height - 120, f"Employment Type: {employment_type}")
    c.drawString(50, height - 140, f"Location: {location}")
    c.drawString(50, height - 160, f"Company Size: {company_size}")
    c.drawString(50, height - 180, f"Remote Ratio: {remote_ratio}")
    c.drawString(50, height - 200, f"Predicted Salary: ${salary}")

    
    try:
        importances = model.feature_importances_
        features = model.feature_names_in_
        top_idx = importances.argsort()[-3:][::-1]
        c.drawString(50, height - 230, "Top 3 Factors Affecting Salary:")
        for i, idx in enumerate(top_idx):
            c.drawString(60, height - 250 - i * 20,
                         f"{i+1}. {features[idx]} ({importances[idx]*100:.1f}%)")
    except Exception:
        pass

    c.save()

    
    return render_template(
        "result.html",
        salary=salary,
        roles=roles,
        role_predictions=role_predictions,
        experience_levels=experience_levels,
        salary_vs_experience=salary_vs_experience,
        pdf_report=pdf_path
    )

if __name__ == "__main__":
    app.run(debug=True)
