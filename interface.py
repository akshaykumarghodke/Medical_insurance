from flask import Flask, render_template,jsonify,request
from project_app.utils import MedicalInsurance
import config

app  = Flask(__name__)

@app.route("/")  
def hello_flask():
    print("Welcome to flask")
    return "Hello Flask"

################################################################################################

@app.route("/predict_charges")
def get_insurance_charges():

    data = request.form 
    age = eval(data["age"])
    sex = data['sex']
    bmi = eval(data["bmi"])
    children = eval(data["children"])
    smoker = data["smoker"]
    region = data["region"]

    print("age,sex,bmi,children,smoker,region",age,sex,bmi,children,smoker,region)

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predicted_charges()

    return jsonify({"Result":f"Predicted Medical Insurance Charges are :{charges}"})






app.run() #server start