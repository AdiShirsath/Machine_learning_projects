# Telco Customer Churn Prediction

## Overview:-
>* In this project we will try to predict if customer in telco will leave or not using machine learning
>* One we predict if customer is going to leave company can take necessary steps to stop customer from leaving

## Data:-
>* We have got data from IBM website to get this visit [here](https://community.ibm.com/accelerators/catalog/content/Telco-customer-churn)
>* This data set contains 7043 observations with 33 variables
>* For detailed information of each column see Data/Data_info.md file

## Training and Evaluation:-
>* For this project we have used 'xgb' aka "XGBOOST" model
>* So all preprocessing is done to work with xgb

>* First xgb_classifier 
>>* this classifier got 80% accuracy for our data
>>* but got less recall and precision 
>>> <img src="https://user-images.githubusercontent.com/75840165/108822172-b71c2380-75e4-11eb-825a-adadeb907b33.png" width="300" height="300"/>
>>>* this model was not predicting better on customers who left(beause of inbalanced dataset)

>* best xgb With grid search we got best params and built ideal xgb model(handling imbalnced using xgb's parmas)
>>* ideal model got 78.64 accuracy
>>* but had better scores in recall and precision on 
>>> <img src="https://user-images.githubusercontent.com/75840165/108822900-bfc12980-75e5-11eb-9721-152249074c12.png" width='300' height='300'/>

>* Here is first tree of ideal_xgb
>> <img src="https://user-images.githubusercontent.com/75840165/108824402-ac16c280-75e7-11eb-988e-7d9c6f4d5861.png" height=300/>

### Saved model:
>>* To get saved model open saved_model folder and download model
>>* for using it import pickel
>>>* use pickel.load(open('pathToModel', 'rb')

### Feature importance
> <img src="https://user-images.githubusercontent.com/75840165/108826112-ed0fd680-75e9-11eb-801d-462a97ff517c.png"/>
