from flask import Flask, render_template, request
import datetime
import numpy as np
import pickle
import requests
import sklearn
from sklearn.preprocessing import StandardScaler

standard_to = StandardScaler()
app = Flask(__name__)

# load the model
model = pickle.load(open('save_model.pkl', 'rb'))

# template
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

# predict
@app.route('/',methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        # year
        Year = int(request.form['Year'])
        Year= datetime.datetime.now().year - Year
        # log_year = np.log(Year)

        # purcahsed price
        showroom_price = float(request.form['purcahsed_Price'])
        # sp_log = np.log(showroom_price)

        # kms
        kms_driven = int(request.form['Kms_Driven'])
        # log_kms = np.log(kms_driven)

        # owner
        Owner=int(request.form['Owner'])
        # log_owner = np.log(Owner)

        # fuel type
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if Fuel_Type_Petrol=='Petrol':
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        elif Fuel_Type_Petrol=='Diesel':
                Fuel_Type_Petrol=0
                Fuel_Type_Diesel=1
        else: 
                Fuel_Type_Petrol=0
                Fuel_Type_Diesel=0

        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if Seller_Type_Individual=='Individual':
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
        
        # transmission
        Transmission_Manual=request.form['Transmission_Manual']
        if Transmission_Manual=='Manual':
            Transmission_Manual=1
        else:
            Transmission_Manual=0

        # prediction    
        prediction=model.predict([[Year, showroom_price, kms_driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
        output=round(prediction[0], 2)

        if output<0:
            return render_template('index.html',prediction_text="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You can sell the Car at {} L".format(output))

    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)