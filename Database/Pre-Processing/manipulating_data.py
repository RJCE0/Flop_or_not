import pandas as pd
import numpy


# Begin with tuples of (y, y-1) where y is the dtabase from year y 
files_dict = {
    "2022-23": "Database/CSVs/FBRefDatabase2022-23.csv",
    "2021-22": "Database/CSVs/FBRefDatabase2021-22.csv",
    "2020-21": "Database/CSVs/FBRefDatabase2020-21.csv",
    "2019-20": "Database/CSVs/FBRefDatabase2019-20.csv",
    "2018-19": "Database/CSVs/FBRefDatabase2018-19.csv",
}
# List = (Y, Y-1)
year_pairs = [(files_dict["2022-23"], files_dict["2021-22"]), 
     (files_dict["2021-22"], files_dict["2020-21"]),
     (files_dict["2020-21"], files_dict["2019-20"]),
     (files_dict["2019-20"], files_dict["2018-19"]),
    ]

df = pd.DataFrame([])

# For every year pair that we have, we want to get the first entry in the tuple which is the 
# file name of the database for that specific year. Then once retrieved we want to go through each entry and
# take the player data for this year and couple it with the team data for the second entry in year pair. 
for year_pair in year_pairs:
    # (files_dict["2022-23"], files_dict["2021-22"])
    df1 = pd.read_csv(year_pair[0])
    df2 = pd.read_csv(year_pair[1])
    for i in range(len(df1)):
        
        # Select the ith entry from the current year of players in the database
        curr_year_player = df1.loc[i]
        
        #Find the current players team 
        team = curr_year_player["Club Name"]
        
        # Find the players stats for the previous campaign if exists 
        prev_year_player = df2[df2["Player Name"] == curr_year_player["Player Name"]]
        
        # If-else check for if player is in prev database if not skip player by breaking from else
        if not prev_year_player.empty:
            # Find the teams squad stats for the previous campaign
            squad_stats_prev_year = df2[df2["Club Name"] == team]
        
            # Removing curr player from prev year squad dataset to ensure unique 15 players
            squad_stats_prev_year = squad_stats_prev_year[squad_stats_prev_year["Player Name"] != curr_year_player["Player Name"]]
            
            # Get top top 15 players by minutes played
            dfe = squad_stats_prev_year.nlargest(15, 'Mins')
        
            # TODO: Combine curr player stats, their prev year, and squad stats to one row
            
        else:
            break



