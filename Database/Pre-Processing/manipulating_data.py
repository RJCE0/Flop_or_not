# %%
import pandas as pd

# %%
file1 = "../CSVs/FBRefDatabase2018-19.csv"
file2 = "../CSVs/FBRefDatabase2019-20.csv"
file3 = "../CSVs/FBRefDatabase2020-21.csv"
file4 = "../CSVs/FBRefDatabase2021-22.csv"
file5 = "../CSVs/FBRefDatabase2022-23.csv"
files = [file1, file2, file3, file4, file5]

# %%
df = pd.read_csv(file1)
df.head(5)

# %% [markdown]
# # Add years to the dataframe

# %%
# This might break other code lol

# i = 0
# for file in files:
#     df = pd.read_csv(file)
#     df["Year"] = i
#     df.to_csv(file, index=False, na_rep='Unknown')
#     i += 1
    

# %% [markdown]
# # The algorithm the combine the data

# %%
# 1. Find a player P
# 2. Find their club C, and the year Y
# 3. Get all of the stats of the Starting 11 for C in the year (Y - 1)
#     You should now have player P's stats in the year Y alongside the starting
#     11 for C in the year (Y - 1). Player P should be playing for C in the year
#     Y.
# 4. Organise that into 1 row in with a fixed length (NN has fixed input)
# 5. From here we can do other things (PCA, Removing rows w mcl, scalling etc)

# Notes:
# - Ideally we would choose all players on a team, but we have to choose a fixed 
# number of players because of the NNs fixed input size
# - If a player only exists in 1 year Y and not in another year Y-1, they will 
# have to be removed from the dataset.

# %% [markdown]
# # 0. Extra stuff

# %%
# finding all clubs
                    # all_clubs = []

                    # for file in files:
                    #     df = pd.read_csv(file)
                    #     all_clubs += list(df["Club Name"])
                    #     # clubs_in_season = set(clubs_in_season)
                    #     # all_clubs.append(clubs_in_season)
                    #     # all_clubs.append(list(df["Club Name"]))

                    # # all_clubs = set(all_clubs)
                    # all_clubs = set(all_clubs)
                    # all_clubs
                    # # set(df["Club Name"])
# restricting positions
                    # df["Position"] = df["Position"].str[:2]


# %% [markdown]
# # 1. Find a player P 
# # 2. Find their club C, and the year Y
# 
# 

# %%
# print(df.iloc[3])
print(df.iloc[3]["Player Name"])
print(df.iloc[3]["Position"])
print(df.iloc[3]["Club Name"])
print(df.iloc[3]["Year"])

name = df.iloc[3]["Player Name"]
pos  = df.iloc[3]["Position"]
club = df.iloc[3]["Club Name"]
year = df.iloc[3]["Year"]

# %% [markdown]
# # 3. Get all of the stats of the Starting 11 for C in the year (Y - 1)
# 

# %%
next_year = year + 1

# %%
# sorting by club and minutes
df.sort_values(by=["Mins"])
df.groupby("Club Name")


# %%
# we have next_year, and the club name 
player_stats = list(df.loc[0][1:-1])
player_stats

# %%
team_df = df[df["Club Name"] == 0]
team_df

# %%
stats_as_list = []
for i in range(min(15,len(team_df))):
    stats_as_list += list(team_df.loc[i][1:-1])

stats_as_list

# %%
# You should now have player P's stats in the year Y alongside the starting
# 11 for C in the year (Y - 1). Player P should be playing for C in the year Y.

# %%
# 4. Organise that into 1 row in with a fixed length (NN has fixed input)
# 5. From here we can do other things (PCA, Removing rows w mcl, scalling etc)

# Notes:
# - Ideally we would choose all players on a team, but we have to choose a fixed 
# number of players because of the NNs fixed input size
# - If a player only exists in 1 year Y and not in another year Y-1, they will 
# have to be removed from the dataset.

# %%



