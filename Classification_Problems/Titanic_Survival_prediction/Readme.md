# Titanic Survival Prediction

## Overview:-
* This is project for predicting if person will survive or not on basis of certain features

## Data:- 
* This dataset is from kaggle you can get it [here](https://www.kaggle.com/c/titanic/data)
* Train set contains 891 records and test set contains 417 records 
* Variable Notes
>* pclass: A proxy for socio-economic status (SES)
>>* 1st = Upper
>>* 2nd = Middle
>>* 3rd = Lower
>* age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5
>* sibsp: The dataset defines family relations in this way...
>* Sibling = brother, sister, stepbrother, stepsister
>* Spouse = husband, wife (mistresses and fiancés were ignored)
>* parch: The dataset defines family relations in this way...
>* Parent = mother, father
>* Child = daughter, son, stepdaughter, stepson
>* Some children travelled only with a nanny, therefore parch=0 for them.


## Preprocessing data:-
* Here we had some features like passengersId, name which had same unique values as len of df
 so this kind of features are not useful in prediction so we drop them.
* Some column had less missing values so replaced them with median
* But cabin feature had more than 70% of missing data so we made NaN as new category 'missing'
* Finally OneHotEncoded categorical features.

## Training and Evaluating Model:-
* Here initially we tested three models Random forest, GradientBoostClassifier and knn on train set and got following scores on validation set

![titanic_acc_compare](https://user-images.githubusercontent.com/75840165/109696160-bc640a00-7bb2-11eb-8e1c-486abb16c4aa.png)

* As we can see randomforest and GBC got better scores so we will hypertune them 

## Hypertuning:- 
* after hyperparameter tunning we got GradientBoostClassifier as best 
*  with this parameters learning_rate= 0.01, max_depth= 4, max_features= 16, min_samples_leaf= 1, min_samples_split= 20,  n_estimators= 500

<img src="https://user-images.githubusercontent.com/75840165/110363121-2c1d3d80-8068-11eb-82b1-4af800cfb9be.png" height=300, width=400/>  <img src="https://user-images.githubusercontent.com/75840165/110363126-2d4e6a80-8068-11eb-8c6d-ae18330b455e.png" height=300, width=400 />


## Feature Importance:-
* Here for our Greadient Boost model feature 'sex' and 'Pclass' were top predictors
![features_titanic](https://user-images.githubusercontent.com/75840165/110363135-2fb0c480-8068-11eb-9ffd-b0d4481f28f8.png)

