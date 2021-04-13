from flask import Flask, request, render_template
import pickle
from flask_cors import cross_origin
import pandas as pd
import sklearn

app = Flask(__name__)
model = pickle.load(open('rf_model.pkl', 'rb'))


@app.route('/')
@cross_origin()
def home_page():
    return render_template('index.html')


@app.route('/Prediction', methods=["GET", "POST"])
@cross_origin()
def predict_page():
    if request.method == "POST":

        # extract features from Date of journey
        dep_date = request.form['Dep_Time']

        Journey_Day = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").day)
        Journey_Month = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").month)

        # Departure time
        Dep_Hour = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").hour)
        Dep_Min = int(pd.to_datetime(dep_date, format="%Y-%m-%dT%H:%M").minute)

        # Arrival time
        arrival_date = request.form["Arrival_Time"]
        Arrival_Hour = int(pd.to_datetime(arrival_date, format="%Y-%m-%dT%H:%M").hour)
        Arrival_Min = int(pd.to_datetime(arrival_date, format="%Y-%m-%dT%H:%M").minute)

        # Duration
        Duration_Hours = abs(Arrival_Hour - Dep_Hour)
        Duration_Min = abs(Arrival_Min - Dep_Min)

        # Get stops
        Total_Stops = int(request.form["stops"])

        # ----------------------
        # getting source info
        Source = request.form["Destination"]
        if Source == 'Delhi':
            sc_Delhi = 1
            sc_Kolkata = 0
            sc_Mumbai = 0
            sc_Chennai = 0

        elif (Source == 'Kolkata'):
            sc_Delhi = 0
            sc_Kolkata = 1
            sc_Mumbai = 0
            sc_Chennai = 0

        elif (Source == 'Mumbai'):
            sc_Delhi = 0
            sc_Kolkata = 0
            sc_Mumbai = 1
            sc_Chennai = 0

        elif (Source == 'Chennai'):
            sc_Delhi = 0
            sc_Kolkata = 0
            sc_Mumbai = 0
            sc_Chennai = 1

        else:
            sc_Delhi = 0
            sc_Kolkata = 0
            sc_Mumbai = 0
            sc_Chennai = 0

        # -------------------------------------------
        # Getting Destination

        Destination = request.form["Destination"]
        if Destination == 'Cochin':
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif Destination == 'Delhi':
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif Destination == 'New_Delhi':
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif Destination == 'Hyderabad':
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif Destination == 'Kolkata':
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        # ---------------------------------------------
        # Get Airline
        airline = request.form['airline']
        if airline == 'Jet Airways':
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif (airline == 'IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline == 'Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0

        elif (airline == 'Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        # make prediction
        prediction = model.predict([[
            Total_Stops,
            Journey_Day,
            Journey_Month,
            Dep_Hour,
            Dep_Min,
            Arrival_Hour,
            Arrival_Min,
            Duration_Hours,
            Duration_Min,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            sc_Chennai,
            sc_Delhi,
            sc_Kolkata,
            sc_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi]])

        # round it to 2 decimals only
        price = round(prediction[0], 2)
        return render_template('prediction.html', prediction=price)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
