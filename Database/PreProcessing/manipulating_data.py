import pandas as pd
import numpy as np
import csv
from .utils.common import year_pairs


dataset = []
n_features = 13
n_fwd = 3
n_mid = 3
n_def = 2

# Begin with tuples of (y, y-1) where y is the dtabase from year y 

# List = (Y, Y-1)

# Function to apply -1 padding if n largest function yields less than n size data required
def n_largest_with_padding(dataFrame, n, category):
    res = dataFrame.nlargest(n, category)
    padding_needed = n - len(res)
    if padding_needed > 0:
        
        # print(f"This is the padding needed: {padding_needed}")
        padding = np.negative(np.ones(shape=(padding_needed, n_features)))
        # print(f"This is the array of zero padding required {padding}")
        
        for minus_array in padding:
            # print(f"This should get the singular row of the zero array: {zero_array}")   
            res.loc[len(res)] = minus_array
    return res

def postion_split(dataFrame, paddingFlag):
    if paddingFlag:
        topFwds = n_largest_with_padding(dataFrame[dataFrame["Position"] == 1], n_fwd, 'Mins')
        topMids = n_largest_with_padding(dataFrame[dataFrame["Position"] == 2], n_mid, 'Mins')
        topDefs = n_largest_with_padding(dataFrame[dataFrame["Position"] == 3], n_def, 'Mins')
        return topFwds, topMids, topDefs
    topFwds = dataFrame[dataFrame["Position"] == 1].nlargest(n_fwd, 'Mins')
    topMids = dataFrame[dataFrame["Position"] == 2].nlargest(n_mid, 'Mins')
    topDefs = dataFrame[dataFrame["Position"] == 3].nlargest(n_def, 'Mins')
    return topFwds, topMids, topDefs

# For every year pair that we have, we want to get the first entry in the tuple which is the 
# file name of the database for that specific year. Then once retrieved we want to go through each entry and
# take the player data for this year and couple it with the team data for the second entry in year pair. 
for year_pair in year_pairs:
    # (files_dict["2022-23"], files_dict["2021-22"])
    df_current_year = pd.read_csv(year_pair[0])
    df_previous_year = pd.read_csv(year_pair[1])
    for i in range(len(df_current_year)):
        
        # Select the ith entry from the current year of players in the database
        curr_year_player = df_current_year.loc[i]
        
        # Find the players stats for the previous campaign if exists 
        prev_year_player = df_previous_year[df_previous_year["Player Name"] == curr_year_player["Player Name"]]
        
        # If-else check for if player is in prev database if not skip player 
        if not prev_year_player.empty:
            # Find the teams squad stats for the previous campaign
            squad_stats_prev_year = df_previous_year[df_previous_year["Club Name"] == prev_year_player["Club Name"].iloc[0]]
        
            # Removing curr player from prev year squad dataset to ensure unique 15 players
            squad_stats_prev_year = squad_stats_prev_year[squad_stats_prev_year["Player Name"] != curr_year_player["Player Name"]]
            
            # Get 13 players with 5, 5, 3 the split; ordered by minutes for each position category
            # Suggestion: Implement for other categories than Minutes? Maybe xAG?
            
            # Apply padding if less than n largest available 
            top_fwds, top_mids, top_defs = postion_split(squad_stats_prev_year, paddingFlag=0)

            # Make one dataframe containing the data for a player's previous season stats and their teammates stats for the previous season
            all_together = pd.concat([prev_year_player, top_fwds, top_mids, top_defs], ignore_index=True)
            curr_year_player = curr_year_player.drop(['Player Name'])
            all_together = all_together.drop(columns=['Player Name'])
        
            # Combine curr player stats and the allTogether dataframe
            curr_year_player_df = curr_year_player.values
            all_together_array = np.array(all_together).reshape(1,-1)
            all_together_array_with_label = [list(curr_year_player) + list(*all_together_array)]
            dataset.append(all_together_array_with_label)


# Function to identify the shape of the data, count how many fit and to print the row itself.
# (Uesful to find shape because variation exists due to missing data in our csvs and we need
# consistency)
# fits, non_fits = 0, 0 
# print(np.array(data))
# for i in np.array(data, dtype=object):
#     if len(i[0]) == 210:
#         print(len(i[0]))
#         fits += 1
#     else:
#         print(i[0])
#         # print("\n\n\n")
#         non_fits += 1
#     print(len(i[0]))
# print(f"fits: {fits} \nnon_fits: {non_fits}")

# Filtering out rows that arent the correct shape
def correct_shape_filter(list, whitelist_len, flag):
    filtered_list = []
    if flag == 1:
        for i in range(len(list)):
            if len(list[i][0]) == whitelist_len:
                filtered_list.append(list[i])
    else:
        for i in range(len(list)):
            if len(list[i]) != whitelist_len:
                filtered_list.append(list[i])
                filtered_list.append(f"Size of list is: {len(list[i][0])}")
    return filtered_list

# Writing the data to a CSV file
tot = (n_fwd + n_mid + n_def + 2)*n_features
filtered_data_list = correct_shape_filter(dataset, tot, 1)
print(len(filtered_data_list))
with open('/home/javonne/Flop_or_not/Database/CSVs/DatasetWithoutPaddingModded.csv', 'w', newline='') as file:
    writer = csv.writer(file, escapechar=' ', quoting=csv.QUOTE_NONE)
    for row in filtered_data_list:
        writer.writerows(row)

