from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age_years = float(request.form['AGE_YEARS'])
        emp_years = float(request.form['EMP_YEARS'])

        features = [
            float(request.form['CODE_GENDER']),
            float(request.form['FLAG_OWN_CAR']),
            float(request.form['FLAG_OWN_REALTY']),
            float(request.form['CNT_CHILDREN']),
            float(request.form['AMT_INCOME_TOTAL']),
            float(request.form['NAME_INCOME_TYPE']),
            float(request.form['NAME_EDUCATION_TYPE']),
            float(request.form['NAME_HOUSING_TYPE']),
            -1 * 365 * age_years,       # Converted Age
            365 * emp_years,            # Converted Employment
            float(request.form['CNT_FAM_MEMBERS']),
            float(request.form['paid_off']),
            float(request.form['#_of_pastdues']),
            float(request.form['no_loan'])
        ]
        prediction = model.predict([features])[0]
        result = "Approved" if prediction == 1 else "Rejected"
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
