# 2022/23 SEASON

from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
html_text = scraper.get('https://fbref.com/en/comps/9/stats/Premier-League-Stats').text
soup = BeautifulSoup(html_text, 'html.parser')
# [(club, club link)]
team_links = []

table = soup.find(id="all_stats_squads_standard")

links = table.find('tbody').find_all('tr')

for link in links:
    player_deets = link.find('th', {'data-stat' : 'team'}).find('a')
    team_links.append((player_deets.text, "https://fbref.com" + player_deets['href']))

# Now we have a list of team links to next extract the player stats from. 
    

# [Name, Age, Pos, Team, starts, mins, goals, non-pen goals, assists, XG, npXG, XA, crdY, crdR]
scraper2 = cloudscraper.create_scraper(delay=15, browser="chrome")
results = []
for (team, link) in team_links:
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
    
print(results)


# table1 = soup.find(id="all_stats_standard").find('div', class_='table_container is_setup')
# print(table1)
# player_list = soup.find('tbody').find_all('tr')

# for player in player_list:
#     name = player.find('td', {'data-stat': 'player'}).find('a').text
#     pos = player.find('td', {'data-stat': 'position'}).text
#     team = player.find('td', {'data-stat': 'team'}).find('a').text
#     age = player.find('td', {'data-stat': 'age'}).text
#     starts = player.find('td', {'data-stat': 'games_starts'}).text
#     minutes = player.find('td', {'data-stat': 'minutes'}).text
#     goals = player.find('td', {'data-stat': 'goals'}).text
#     assists = player.find('td', {'data-stat': 'assists'}).text
#     non_pen_goals = player.find('td', {'data-stat': 'goals_pens'}).text
#     crdY = player.find('td', {'data-stat': 'cards_yellow'}).text
#     crdR = player.find('td', {'data-stat': 'cards_red'}).text
#     xG = player.find('td', {'data-stat': 'xg'}).text
#     npXG = player.find('td', {'data-stat': 'npxg'}).text
#     xA = player.find('td', {'data-stat': 'xg_assist'}).text
#     results.append([name, pos, team, age, starts, minutes, goals, non_pen_goals, assists, crdY, crdR, xG, npXG, xA])
    
# print(results)
    