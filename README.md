# Machine_learning_projects

## Overview:-
* This repository contains projects on ML Classification and Regression
>* [Classification](https://en.wikipedia.org/wiki/Statistical_classification):-  classification is the problem of identifying to which of a set of categories (sub-populations) a new observation belongs, 
on the basis of a training set of data containing observations (or instances) whose category membership is known.
>>* Ex. Prediction of heart disease( Yes or No)

![classification](https://user-images.githubusercontent.com/75840165/109419751-04d5c900-79f5-11eb-93b6-004d2875116b.png)
------------------------------------------------------------------

>* [Regression](https://en.wikipedia.org/wiki/Regression_analysis):- In statistical modeling, regression analysis is a set of statistical processes for estimating the relationships between a dependent 
variable (often called the 'outcome variable') and one or more independent variables (often called 'predictors', 'covariates', or 'features').
>>* Ex. Prediction of number (price prediction)

![Regression](https://user-images.githubusercontent.com/75840165/109419745-ff787e80-79f4-11eb-9f1d-55646eb0dce8.png)
--------------------------------------------------

## Repository Guide:-
Here is list for every project in this repository and link to introduction of project

--------------------------------------------------
### Classification:-
* <a href='#Telco-churn'>Telco Customers Churn Prediction</a>
* <a href="#Heart-dis">Heart Disease Prediction</a>
* <a href="#Titanic">Titanic Survival Prediction</a>

### Regression:-
* <a href='#Bulldozers'>Bulldozers Price Prediction<a>
* <a href="#House-price">House Price Prediction</a>
* <a href="#Flight-fare">Flight Fare Prediction (Web-App)</a>

## Tools And Workflow:-

![machine-learning-life-cycle](https://user-images.githubusercontent.com/75840165/114572787-6dbb8c80-9c95-11eb-8865-d8bf0d677f68.png)

* Collect Data
* Exploratory Data Analysis:- (with visualization)
>>* Pandas, Matplotlib, [Seaborn](https://seaborn.pydata.org/)
* Feature Engineering:-
>* Handle missing values and Categorical Features - sklearn
>* Outlier's (depending on which model to use)
>* Feature Scaling (depending on model)
* Split data
* Feature selection:-
>* Correlation matrix, [VariationThreshold](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html)
* Building model 
>* [Selecting models](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)
>* Train and Evaluate model
>* If more than one depending on initial accuracy take for Hyperparameter Tuning - [RandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV), [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
* Predict on test set
* Build web-app Flask, HTML5, CSS3 or Streamlit
* Deploy on cloud

<img src="https://user-images.githubusercontent.com/75840165/109416819-79553b80-79e6-11eb-9b75-a0861894af1c.png" height=500, width=700/>

## Project Introduction's:-(for detail discription visit respective project)

### Classification:-
-----------------------------------------------
<h4 id='Telco-churn'>Telco Churn Predictor<h4>

* This project is to predict if customer will leave telco or not, using machine learning
* In this we used XGBoost classifier to predict it and got 78.64 accuracy
>* by using  gamma=0, learning_rate=0.1, max_depth=4, reg_lambda=10, scale_pos_weight=2, subsample=0.9, colsample_bytree=0.5, which we got by hyperparameter tunning XGBClassifier
* Get source code [Visit][Telco-churn]

<h4 id='Heart-dis'> Heart Disease Predictor</h4>

* On basis of person's health records predict if person have heart disease or not
* In this we used 4 different models to see initial accuracy (ie. SVM, RandomForestClassifier, Adaboost, KNN)
>* Out of this we we picked top two for hypertunning( RandomForest and Adaboost) and Adaboost got 91% accuracy_score
* Get source code [Visit][Heart-dis]

<h4 id='Titanic'> Titanic Survial Predictor</h4>

* This project is to predict the passangers in titanic will survive or not on the basis of given data.
* In this notebook we've used Random Forest,KNN and GradientBoost classifier and got better accuracy on these top 2 models i.e.GradientBoostClassifier and RandomForestlassifier.
* After Hypertunning got an accuracy 78.73% for Gradient Boosting.
>* Hypertunnig parameters for GBC learning_rate= 0.01, max_depth= 4, max_features= 16, min_samples_leaf= 1, min_samples_split=20, n_estimators= 500.
* Get source code [Visit][Titanic]

### Regression:-
------------------------------------------------------------------
<h4 id='Bulldozers'> Bulldozer Price Predictor</h4> 

* Prediction of sale price of bulldozer on basis of its specifications like year made, productSize and 50 more features 
* Here we used RandomForestRegressor and got pretty good score of 85% r^2 
* so after hypertuning we got best_params n_estimators=90, min_samples_leaf=1, min_samples_split=14,max_features=0.5, n_jobs=-1, max_samples=None 
* with this we got 95% and 88% r^2 on train and test set respectively
* Get source code [Visit][Bulldozers]


<h4 id='House-price'> House Price Predictor</h4>

* Prediction of House price on basis of features of house
* Here we used Lasso, randomforest and XGBoost for initial r^2 score
* Then we hypertuined XGB cause it had bit more r^2 and got gamma= 0, learning_rate= 0.05, max_depth =6, reg_lambda= 0, subsample=0.9, colsample_bytree=0.5
* with this params I got 98% and 85% r^2 on train and validation set respectively
* Get source code [Visit][House-price]


<h4 id='Flight-fare'> Flight Fare Prediction <h4>

* Predicting fare of flight based on given information
* Trained Lasso, Gradient Bosst, Random Forest on full data
* Random forest had best 80 r2 so took this for hyperparameter tuning got 83 r2
* Using ***Flask*** with help of html5-css3 built web-app and Deployed on ***Heroku***
* To view ***demo*** of web app [visit][Flight-fare]
  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------







<!-- Classification Links-->
[Telco-churn]: https://github.com/AdiShirsath/Machine_learning_projects/tree/main/Classification_Problems/Telco_churn_prediction
[Titanic]: https://github.com/AdiShirsath/Machine_learning_projects/tree/main/Classification_Problems/Titanic_Survival_prediction
[Heart-dis]: https://github.com/AdiShirsath/Machine_learning_projects/tree/main/Classification_Problems/Prediction_of_heart_disease

<!-- regression Links-->
[Bulldozers]: https://github.com/AdiShirsath/Machine_learning_projects/tree/main/Regression_Problems/Bulldozers_price_prediction_project
[House-price]: https://github.com/AdiShirsath/Machine_learning_projects/tree/main/Regression_Problems/House_price_prediction
[Flight-fare]: https://github.com/AdiShirsath/Machine_learning_projects/tree/main/Regression_Problems/Flight_Fare_Prediction
