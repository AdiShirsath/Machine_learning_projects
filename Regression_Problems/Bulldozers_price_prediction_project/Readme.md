# Bulldozer Price Prediction

## Overview:-
>* This project is to predict price of bulldozer using different features in dataset
>* We are predicting numeric value so this kind of problem is Regression problem
>* This project is having time serise data so we'll do split according that

## Goal:-
>* Here our goal is to predict price of bulldozer's 

## Data:- 
>* We got the data from kaggle competition
>* In this case, it's historical sales data of bulldozers. Including things like, model type, size, sale date and more.
>>* Details of data is in [Data.md file](https://github.com/AdiShirsath/Machine_learning_projects/blob/main/Regression_Problems/Bulldozers_price_prediction_project/Data.md)

## Preprocessing Data:-
>* Here we replaced nan for numerical columns with median. 
>* for categorical columns we used pandas category which converts features dtype from object to category.
>* Pandas category converts nan with -1 so we added 1 in every value.
>* for this we spitted data using saleyear before 2012 all train set and 2012 was validation set. 

## Training and Evaluation
>* Here we tried RandomForestRegressor at first
>>* Got  this scores
>>> 'Training MAE': 5527.459402081646,
>>> 'Valid MAE': 7038.722370171953,
>>> 'Training RMSLE': 0.2574159257311189,
>>> 'Valid RMSLE': 0.28857034786321156,
>>> 'Training R^2': 0.8625735886280191,
>>> 'Valid R^2': 0.8377235697687395
>* It was good score so I did hypertuining o randomforest.
>* Here is residual plot for this
![random_residual](https://user-images.githubusercontent.com/75840165/109691612-9f790800-7bad-11eb-8b4a-972af7735a28.png)

### Hyperparameter Tuining:- 
>* Here first I did RandomSearchCV after observing parameters for this, updated param grid. 
>* with updated param Grid ran GridSearchCV on it
>* best parameters were n_estimators=90, min_samples_leaf=1, min_samples_split=14,max_features=0.5,n_jobs=-1,max_samples=None
>* updated Scores
>>> 'Training MAE': 2977.237280450033,
>>> 'Valid MAE': 5893.235758456529,
>>> 'Training RMSLE': 0.14578777354605765,
>>> 'Valid RMSLE': 0.2427619595854995,
>>> 'Training R^2': 0.9583654753712876,
>>> 'Valid R^2': 0.8827605894013926

>* Residual plot for this
![residual_ideal](https://user-images.githubusercontent.com/75840165/109691701-b91a4f80-7bad-11eb-9886-66df13bcd8f5.png)


## Feature importance:-
>* Here year made, product size and sale year was top three features in prediction of bulldozer's price

![Bulldozers_feature_imp](https://user-images.githubusercontent.com/75840165/109691774-cd5e4c80-7bad-11eb-8101-f60776cbfff6.png)


