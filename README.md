<img src="https://github.com/RJCE0/Flop_or_not/blob/main/logo.PNG" width="400">

A machine learning prediction model that predicts the number of **goals** a current Premier League player will score in the Upcoming **23/24 season**

## Source
All data has been web-scrapped from FBRef for the following premier league seasons:
* [2018/19](https://fbref.com/en/comps/9/2018-2019/stats/2018-2019-Premier-League-Stats "Premier League player data from 2018/19")
* [2019/20](https://fbref.com/en/comps/9/2019-2020/stats/2019-2020-Premier-League-Stats "Premier League player data from 2019/20")
* [2020/21](https://fbref.com/en/comps/9/2020-2021/stats/2020-2021-Premier-League-Stats "Premier League player data from 2020/21")
* [2021/22](https://fbref.com/en/comps/9/2021-2022/stats/2021-2022-Premier-League-Stats "Premier League player data from 2021/22")
* [2022/23](https://fbref.com/en/comps/9/2022-2023/stats/2022-2023-Premier-League-Stats "Premier League player data from 2022/23")


## Installation

`pip install requirements.txt`

## Scrapped Data
For our prediction model we focused primarily on data in relation to goal scoring metrics and the metrics that would influence a players ability to score goals. We collect the following data from each of the years for the player:

1. Name
2. Position
3. Club
4. Age
5. No. Starts
6. No. Minutes
7. Goals
8. Non-Penalty Goals
9. Assists
10. No. Yellow Cards
11. No. Red Cards
12. Expected Goals, xG
13. Expected Non-Penalty Goals, npxG
14. Expected Assists, xA

## Data Cleaning
In the data cleaning phase, we transform the raw data extracted from the CSV and turn them into Pandas dataframes.
These are the following transformations performed to the data:
* `Removed` all *Goalkeepers* from the data (Very few are goal scorers lol)
* `One-Hot encoding` to the *Clubs* to turn them into quantitative data
* `Removed` the second and subsequent *Positions* for players that had multiple positions
* `One-Hot encoding` for *Positions*
* Turn *Minutes Played* data into `int` values
* Turn *Age* data into `int` values
  

## Data Manipulating
In the data manipulating phase, the focus was on formatting the data into tensors for the model. We format each row of the tensor as the following. The first 13 columns contain the 14 scraped data entries minus the name for the current season. The next 13 columns are for the same player, only data for the season prior. We also supply each row with 13 other player data split into the following: 

- 5x Forwards
- 5x Midfielders
- 3x Defenders   

The players are ordered by *Minutes Played* since the players with the most minutes contribute most to the general stats of the team. 
**This process is then repeated for all the season pairs that exist for the 2018/19 to 2022/23 Premier League seasons.**

###### Padding
We were at a cross-roads between a sufficient amount of data and a complete set of data. To test which outcome would influence the models more, we created two datasets, the first dataset with 0 padding (also tested -1 padding) to entries where data was missing and a second dataset with fewer entries and features as missing data entries were omitted.  

## Data Loading
Once the data had been transformed in the cleaning and manipulating phases, we use the data loading file to firstly, seperate the labels and inputs then, apply normalisation and dimensionality reduction techniques. 
### Normalisation
We implemented Z-score normalisation using standard scaler and split the data using train_test_split to provide us with the input training set, input test set, label training set and label test set. we normalise the data because this helps our model to learn more easily in training. This is because it can be difficult to compare features when they are different scales. The reason for z-score normalisation in particular is because it handles outliers in data well. 
### Principle Component Analysis
Furthermore we implemented the Principal Component Analysis along with scree plots to find the ideal number of features that truly influence the other statistics. We find the ideal number of prinicple components to be 38. 
## Models
We opted to experiment between two primary models for prediction, a Neural Network regression model and XGBoost with aims to compare both accuracy and speed at which they can offer reliable predictions for the number of goals a player will get in the 23/24 Premier League campaign. We used the Root Mean Squared Error (RMSE) as our metric to indicate how far off the models prediction was from the true value of the test set. 
### Neural Network
We implemented a Deep Neural Network (DNN) to predict the each of the 13 statistics that we tracked. The DNN had 4 hidden layers, and 28 input nodes due to PCA. It had 13 output nodes but we only evaluated the models performance based on the goal prediction. 
Since this was a regression task the loss function was MSE and the Optimisation was Adam. Normalisation was vital to ensuring the model worked as expected (Which we tested using RMSE as well as directly observing the predictions).

|      | w/ Padding  | w/o Padding |
| ---- |:-----------:|:------------|
| RMSE:| ~2.95 Goals | ~3.28 Goals |

### XGBoost
An XGBoost model (eXtreme Gradient Boosting) is simply a tree ensemble whereby new models are added to correct the errors made by existing trees. Tree models are added sequentially until no further improvements can be made. 
We then developed an XGBoost model to try and beat the performance of the Deep Neural Network architecture model. Again we apply PCA and Z-score normalisation to the trainig and testing data. Lastly we use the RMSE metric to identify how accurate the predicted goals were.

|      | w/ Padding  | w/o Padding |
| ---- |:-----------:|:------------|
| RMSE:| ~3.04 Goals | ~2.82 Goals |


## Future Work 
- Hyperparameter optimisation using Bayesian Optimisation hyperparameter tuning
- Implement early stopping criterion
- Implement K-Fold cross-validation
