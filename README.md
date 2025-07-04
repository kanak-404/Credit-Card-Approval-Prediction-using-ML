Credit Card Approval Prediction 📊

A machine learning-powered web application that predicts whether a credit card application will be approved or rejected based on user-provided demographic, financial, and credit behavior data.


🔎 Overview

This project integrates a trained machine learning model into a Flask-based web interface. It enables users to enter personal and financial details and receive an instant prediction about their credit card approval status.

Key components include:

Feature Engineering & Preprocessing of combined datasets

Handling class imbalance using SMOTE

Custom target label generation based on repayment history

Flask app with styled frontend and result visualization


📄 Project Structure

ML_Project/
├── README.md                        # Project documentation
├── .gitignore                      # Ignored files
├── requirements.txt               # Python dependencies
├── app.py                          # Flask application
├── model.pkl                       # Trained ML model
├── templates/                      # HTML templates
│   ├── index.html                  # Project description
│   ├── form.html                   # User input form
│   └── result.html                 # Prediction result page
├── Credit_Card_Approval_Prediction.ipynb  # Model training notebook
├── application_record.csv         # Applicant info dataset
├── credit_record.csv              # Credit history dataset


🛠️ Technologies Used

Python, Flask

HTML5, CSS3

Scikit-learn, Pandas, NumPy

SMOTE (imbalanced-learn)

Seaborn & Matplotlib (for EDA)


🚀 How to Run

Clone the repository

git clone https://github.com/kanak-404/Credit-Card-Approval-Prediction-using-ML.git
cd Credit-Card-Approval-Prediction-using-ML

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

Visit in browser
http://127.0.0.1:5000


📉 Model Details

Final model: GradientBoostingClassifier

Balanced via SMOTE

Feature set includes:

Gender, Car/Property ownership, Income

Age, Employment, Education

Loan repayment history (custom engineered)

📆 Future Improvements

Add user authentication

Save prediction history

Visual dashboard of approvals/rejections

✍️ Author

Kanak Soni

Built as a part of ML coursework project

🚫 Disclaimer

This tool is for academic and educational purposes only and should not be used for real financial decision-making.

