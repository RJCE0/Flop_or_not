from pathlib import Path

# def get_project_root()-> Path:
#     return Path(__file__).parent.parent


files_dict = {
    "2022-23": "Database/CSVs/raw_data/FBRefDatabase2022-23.csv",
    "2021-22": "Database/CSVs/raw_data/FBRefDatabase2021-22.csv",
    "2020-21": "Database/CSVs/raw_data/FBRefDatabase2020-21.csv",
    "2019-20": "Database/CSVs/raw_data/FBRefDatabase2019-20.csv",
    "2018-19": "Database/CSVs/raw_data/FBRefDatabase2018-19.csv",
}

positions_dict = {
    "DF": 3,
    "MF": 2,
    "FW": 1,
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

year_pairs = [(files_dict["2022-23"], files_dict["2021-22"]), 
     (files_dict["2021-22"], files_dict["2020-21"]),
     (files_dict["2020-21"], files_dict["2019-20"]),
     (files_dict["2019-20"], files_dict["2018-19"]),
    ]