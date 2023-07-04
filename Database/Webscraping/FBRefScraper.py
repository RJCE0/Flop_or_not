# Generalised scrapper

from bs4 import BeautifulSoup
import cloudscraper
import numpy as np
import pandas as pd

links_dict = {"2022-23": "https://fbref.com/en/comps/9/stats/Premier-League-Stats",
              "2021-22": "https://fbref.com/en/comps/9/2021-2022/stats/2021-2022-Premier-League-Stats",
              "2020-21": "https://fbref.com/en/comps/9/2020-2021/stats/2020-2021-Premier-League-Stats#all_stats_standard",
              "2019-20": "https://fbref.com/en/comps/9/2019-2020/2019-2020-Premier-League-Stats",
              "2018-19": "https://fbref.com/en/comps/9/2018-2019/stats/2018-2019-Premier-League-Stats",
              }


def scrape_squads_by_year(link):
    scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
    html_text = scraper.get(link).text
    soup = BeautifulSoup(html_text, 'html.parser')
    # [(club, club link)]
    team_links_list = []

    table = soup.find(id="all_stats_squads_standard")

    links = table.find('tbody').find_all('tr')

    for link in links:
        player_deets = link.find('th', {'data-stat' : 'team'}).find('a')
        team_links_list.append((player_deets.text, "https://fbref.com" + player_deets['href']))
        
    # Now we have a list of team links to next extract the player stats from. 
    return team_links_list

def scrape_players_from_team(team_links_list):
    # [Name, Age, Pos, Team, starts, mins, goals, non-pen goals, assists, XG, npXG, XA, crdY, crdR]
    scraper2 = cloudscraper.create_scraper(delay=15, browser="chrome")
    results = []
    for (team, link) in team_links_list:
        html_text2 = scraper2.get(link, allow_redirects=False).text
        player_data_soup = BeautifulSoup(html_text2, 'html.parser')
        player_list = player_data_soup.find(id='div_stats_standard_9').find('tbody').find_all('tr')
        for player in player_list:
            name = player.find('th', {'data-stat': 'player'}).find('a').text
            pos = player.find('td', {'data-stat': 'position'}).text
            age = player.find('td', {'data-stat': 'age'}).text
            starts = player.find('td', {'data-stat': 'games_starts'}).text
            minutes = player.find('td', {'data-stat': 'minutes'}).text
            goals = player.find('td', {'data-stat': 'goals'}).text
            assists = player.find('td', {'data-stat': 'assists'}).text
            non_pen_goals = player.find('td', {'data-stat': 'goals_pens'}).text
            crdY = player.find('td', {'data-stat': 'cards_yellow'}).text
            crdR = player.find('td', {'data-stat': 'cards_red'}).text
            xG = player.find('td', {'data-stat': 'xg'}).text
            npXG = player.find('td', {'data-stat': 'npxg'}).text
            xA = player.find('td', {'data-stat': 'xg_assist'}).text
            results.append([name, pos, team, age, starts, minutes, goals, non_pen_goals, assists, crdY, crdR, xG, npXG, xA])
        
    return results

if __name__ == '__main__':
    for year in list(links_dict.keys()):
        teams = scrape_squads_by_year(links_dict[year])
        players_by_year = scrape_players_from_team(teams)
        array = np.array(players_by_year)
        df = pd.DataFrame({'Player Name': array[:, 0], 'Position': array[:, 1], 'Club Name': array[:, 2],
                           'Age': array[:, 3],'Starts': array[:, 4], 'Mins': array[:, 5], 'Goals': array[:, 6],
                           'npG': array[:, 7], 'Assists': array[:, 8], 'crdY': array[:, 9], 'crdR': array[:, 10],
                           'xG': array[:, 11], 'npXG': array[:, 12], 'xA': array[:, 13]})
        file = f"Database/FBRefDatabase{year}.csv"
        df.to_csv(file, index=False, na_rep='Unknown')