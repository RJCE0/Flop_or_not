import pandas as pd

files_dict = {
    "2022-23": "Database/CSVs/FBRefDatabase2022-23.csv",
    "2021-22": "Database/CSVs/FBRefDatabase2021-22.csv",
    "2020-21": "Database/CSVs/FBRefDatabase2020-21.csv",
    "2019-20": "Database/CSVs/FBRefDatabase2019-20.csv",
    "2018-19": "Database/CSVs/FBRefDatabase2018-19.csv",
}

positions_dict = {
    "DF": 0,
    "MF": 1,
    "FW": 2,
}

clubs_dict = {
    "Arsenal": 0,
    "Aston Villa": 1,
    "Bournemouth": 2,
    "Brentford": 3,
    "Brighton": 4,
    "Burnley": 5,
    "Cardiff City": 6,
    "Chelsea": 7,
    "Crystal Palace": 8,
    "Everton": 9,
    "Fulham": 10,
    "Huddersfield": 11,
    "Leeds United": 12,
    "Leicester City": 13,
    "Liverpool": 14,
    "Manchester City": 15,
    "Manchester Utd": 16,
    "Newcastle Utd": 17,
    "Norwich City": 18,
    "Nott'ham Forest": 19,
    "Sheffield Utd": 20,
    "Southampton": 21,
    "Tottenham": 22,
    "Watford": 23,
    "West Brom": 24,
    "West Ham": 25,
    "Wolves": 26,
}


for file in list(files_dict.values()):
    df = pd.read_csv(file)
    # Remove all Keepers from the database
    df = df.query("Position != 'GK'")
    
    # Remove second positon from all players in database
    df["Position"] = df["Position"].str[:2]
    
    # Remove commas and turn minutes to actual ints
    df["Mins"] = df["Mins"].astype("string")
    df['Mins'] = df['Mins'].str.replace(',', '').astype(int)
    
    # Convert ages to ints since some are floats
    df['Age'] = df["Age"].astype(int)
    
    # Removing year column from dataframe
    df = df.drop(columns=["Year"])
    
    # Convert positions into integers using one-hot encoding
    df = df.replace({"Position": positions_dict})
    # Convert teams into integers using one-hot encoding
    df = df.replace({"Club Name": clubs_dict})

    # Write dataframe back to file
    df.to_csv(file, index=False, na_rep="Unknown")
