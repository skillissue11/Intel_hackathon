from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load your model (adjust the path if necessary)
model = joblib.load('model/employee_attrition_model.joblib')
encoded_columns = joblib.load('model/encoded_columns.joblib')

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convert the input data to the format your model expects
    input_features = np.array([
        data['employeeAge'],
        data['yearsAtCompany'],
        data['yearsWithCurrManager'],
        data['yearsSinceLastPromotion'],
        data['yearsInCurrentRole'],
        data['workLifeBalance'],
        data['trainingTimesLastYear'],
        data['jobSatisfaction'],
        data['education'],
        data['distanceFromHome']
    ]).reshape(1, -1)

    # Make the prediction
    prediction = model.predict(input_features)

    # Prepare the response
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
