# 💼 ML Salary Predictor – Your Career Insights Companion

**Predict. Compare. Analyze. Plan.**  
A sleek, interactive web app powered by Machine Learning that helps users forecast their salary, compare it with industry benchmarks, and explore how experience and roles can shape their future—all with actionable recommendations and downloadable reports!

---

## 🚀 **Why This Project?**

Navigating your career can be overwhelming. Salaries vary by role, experience, and location, and knowing where you stand is crucial for making informed decisions. This project brings data science into the real world by offering personalized, explainable salary predictions with practical advice and detailed reports.

This isn’t just another calculator—it’s an **intelligent career companion** built with machine learning and designed to give you clarity and confidence.

---

## ✨ **Key Features**

✅ **ML-Powered Salary Prediction**  
Based on job title, experience level, location, company size, and more.

✅ **Current Salary Comparison**  
Receive insights on how your current compensation stacks up against market averages.

✅ **Dynamic Role Insights**  
See how changing roles like *Data Scientist* or *ML Engineer* impacts your earning potential.

✅ **What-if Analysis**  
Explore how experience progression from entry-level to executive influences your salary.

✅ **Explainable Results**  
Top factors affecting your salary are highlighted, helping you understand model behavior.

✅ **Downloadable PDF Reports**  
Generate professional reports summarizing predictions, recommendations, and analysis.

✅ **Interactive FAQ Chatbot**  
Get quick answers to common career questions powered by keyword matching.

---

## 🧠 **Tech Stack**

- **Backend:** Python, Flask  
- **Machine Learning:** scikit-learn (model trained using real datasets)  
- **Data Handling:** Pandas  
- **File Generation:** ReportLab (PDF reports)  
- **Frontend:** HTML, CSS, Bootstrap (optional customization)  
- **Version Control:** Git & GitHub  

---

## 📊 **ML Workflow**

1. Trained a regression model (`salary_model.pkl`) using industry data.
2. Engineered features to balance categorical and numerical inputs.
3. Designed an interactive interface where users can explore predictions and trends.
4. Implemented interpretability using feature importance and explainable outputs.
5. Packaged everything into a deployable Flask app with dynamic reporting.

---

## 📂 **Project Structure**

ML_Salary_Predictor_Flask_App/
├── model/ # Trained ML model file
├── static/ # Static assets and generated reports
│ └── reports/ # Auto-generated PDF files
├── templates/ # HTML templates
│ ├── index.html
│ ├── result.html
│ └── chatbot.html
├── faq.json # FAQ data for chatbot
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 📂 **How to Run Locally**

1. Clone the repository:
   ```bash
   git clone https://github.com/RobinChahal0010/ML_Salary_Predictor_Flask_App.git
   cd ML_Salary_Predictor_Flask_App
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open http://localhost:5001 in your browser.
