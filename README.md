# Flop or Not 

A machine learning prediction model that predicts the number of **goals** a current Premier League player will score in the Upcoming **23/24 season**
-----

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

The players are ordered by *Minutes Played* since the players with the most minutes contribute most to the general stats of the team. For any row entires that didn't have correct shape, i.e. there wasn't enough data for the number of Forwards, Midfielders or Defenders we required, we added PADDING (May change this)
**This process is then repeated for all the season pairs that exist for the 2018/19 to 2022/23 Premier League seasons.**

## Data Loading
### Normalisation
### Principle Component Analysis

## Models


