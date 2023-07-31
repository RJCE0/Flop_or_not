import pickle

# Object to be pickled
my_object = None
my_object_name = None

# Pickle the object
with open(f"{my_object_name}.pkl", "wb") as file:
    pickle.dump(my_object, file)


# dont scroll down...






























#dont look at the preview window on the right side.....























































































































































































































# :(







# import pandas as pd
# import numpy as np

# big_list = []

# # Begin with tuples of (y, y-1) where y is the dtabase from year y 
# files_dict = {
#     "2022-23": "Database/CSVs/FBRefDatabase2022-23.csv",
#     "2021-22": "Database/CSVs/FBRefDatabase2021-22.csv",
#     "2020-21": "Database/CSVs/FBRefDatabase2020-21.csv",
#     "2019-20": "Database/CSVs/FBRefDatabase2019-20.csv",
#     "2018-19": "Database/CSVs/FBRefDatabase2018-19.csv",
# }
# # List = (Y, Y-1)
# year_pairs = [(files_dict["2022-23"], files_dict["2021-22"]), 
#      (files_dict["2021-22"], files_dict["2020-21"]),
#      (files_dict["2020-21"], files_dict["2019-20"]),
#      (files_dict["2019-20"], files_dict["2018-19"]),
#     ]

# # dataset = np.array()

# # For every year pair that we have, we want to get the first entry in the tuple which is the 
# # file name of the database for that specific year. Then once retrieved we want to go through each entry and
# # take the player data for this year and couple it with the team data for the second entry in year pair. 
# for year_pair in year_pairs:
#     # (files_dict["2022-23"], files_dict["2021-22"])
#     df1 = pd.read_csv(year_pair[0])
#     df2 = pd.read_csv(year_pair[1])
#     for i in range(len(df1)):
        
#         # Select the ith entry from the current year of players in the database
#         curr_year_player = df1.loc[i]
        
#         #Find the current players team 
#         team = curr_year_player["Club Name"]
        
#         # Find the players stats for the previous campaign if exists 
#         prev_year_player = df2[df2["Player Name"] == curr_year_player["Player Name"]]
        
#         # If-else check for if player is in prev database if not skip player by breaking from else
#         if not prev_year_player.empty:
#             # Find the teams squad stats for the previous campaign
#             squad_stats_prev_year = df2[df2["Club Name"] == team]
        
#             # Removing curr player from prev year squad dataset to ensure unique 15 players
#             squad_stats_prev_year = squad_stats_prev_year[squad_stats_prev_year["Player Name"] != curr_year_player["Player Name"]]
            
#             # Get top 15 players by minutes played 5 per position
#             topFwds = squad_stats_prev_year[squad_stats_prev_year["Position"] == 2].nlargest(5, 'Mins')
            
#             # add zero padding for extra rows in dataset.???
#             # Apply padding if less than n largest available ((14*5)-len(topFwds))
#             # padding_needed = 14*5 - len(topFwds)
#             # if padding_needed != 0:
#             #     padding = np.zeros(padding_needed)
#             #     topFwds.loc[len(topFwds)] = padding
            
            
#             topMids = squad_stats_prev_year[squad_stats_prev_year["Position"] == 1].nlargest(5, 'Mins')
#             # Apply padding if less than n largest available
#             topDefs = squad_stats_prev_year[squad_stats_prev_year["Position"] == 0].nlargest(3, 'Mins')
#             # Apply padding if less than n largest available

#             # get by xAG90
#             # topFwds = squad_stats_prev_year[squad_stats_prev_year["Position"] == 2].nlargest(5, 'xAG90')
#             # topMids = squad_stats_prev_year[squad_stats_prev_year["Position"] == 1].nlargest(5, 'xAG90')
#             # topDefs = squad_stats_prev_year[squad_stats_prev_year["Position"] == 0].nlargest(3, 'xAG90')
            
#             # Get top 15 players by minutes
#             # top15 = squad_stats_prev_year.nlargest(15, 'Mins')

#             # Get top 15 players by minutes, unsorted
#             # top15 = squad_stats_prev_year.nlargest(15, 'Mins')
#             # top15 = top15.sample(frac=1, random_state=42) #pd.DataFrame(curr_year_player) # print(allTogether.head(30))
            
#             # print("----------------------------------------------------------------")
#             allTogether = pd.concat([prev_year_player, topFwds, topMids, topDefs], ignore_index=True)
           
#             # print(allTogether.head())
#             #allTogether.drop(columns=['Player Name', 'Year'])
#             #print(topFwds)
        
#             # TODO: Combine curr player stats, their prev year, and squad stats to one row
#             # Take curr player stats as a row
#             # Iterate through allTogether
#             # Rename each coloumn and Join to curr player row
#             curr_year_player_df = curr_year_player.values
#             allTogether_array = np.array(allTogether).reshape(1,-1)

#             allTogether_array_with_label = [list(curr_year_player) + list(*allTogether_array)]

#             big_list.append(allTogether_array_with_label)
#             # tot = np.concatenate((curr_year_player_df, allTogether_array[0]))
#             # dataset = np.append(dataset, list(tot), axis=0)
#             # dataset = np.vstack((dataset, tot))

#         # else:
#         #     print("hecc")
#             # break




# # print(big_list)
# print(np.array(big_list, dtype=object).shape)

# fits = 0
# non_fits = 0
# # print(np.array(big_list))
# for i in np.array(big_list, dtype=object):
#     if len(i[0]) == 210:
#         fits += 1
#     else:
#         print(i[0])
#         # print("\n\n\n")
#         non_fits += 1
#     print(len(i[0]))

# print(f"fits: {fits} \nnon_fits: {non_fits}")
# # print(np.array(dataset, dtype=object).shape)