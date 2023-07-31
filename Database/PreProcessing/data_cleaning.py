import pandas as pd
from utils.common import files_dict
from utils.common import positions_dict
from utils.common import clubs_dict

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
