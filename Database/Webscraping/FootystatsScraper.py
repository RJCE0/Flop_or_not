from bs4 import BeautifulSoup
import cloudscraper
#import csv
import numpy as np
import pandas as pd

link = None

scraper = cloudscraper.create_scraper(delay=10, browser="chrome")
html_text = scraper.get('https://footystats.org/england/premier-league').text
soup = BeautifulSoup(html_text, 'html.parser')

teams = soup.find_all('td', class_= 'team borderRightContent')

teams_dict = {}
# A list of all the players in the league and their respective clubs and link to their page
player_list = []
# Arsenal -> link for Arsenal

# Arsenal -> [saka link, martinelli link etc]

# team names = team.find('a').text


for team in teams:
    teams_dict[team.find('a').text] = "https://footystats.org" + team.find('a')['href']


scraper1 = cloudscraper.create_scraper(delay=15, browser="chrome")
for team_key in teams_dict.keys():
    team_link = teams_dict.get(team_key)
    html_text1 = scraper1.get(team_link).text
    teams_player_soup = BeautifulSoup(html_text1, 'html.parser')
    players = teams_player_soup.find_all('div', class_= 'w94 rw100 cf m0Auto')
    for player in players:
        player_deets = player.find('p', class_= 'col-lg-6 ellipses').find('a')
        player_name, player_link = player_deets.text, player_deets['href']
        player_list.append((team_key, player_name, "https://footystats.org" + player_link))

# player_list[0] = [('Manchester City FC', 'Erling Haaland', 'https://footystats.org/players/norway/erling-haaland')]

results = []
# list of (team_name, name, postion, salary)
# ('Nottingham Forest FC', 'Willy Boly', 'Defender - Centre Back', '€2,600,000')

scraper2 = cloudscraper.create_scraper(delay=30, browser="chrome")
for (team_name, name, link) in player_list:
    html_text2 = scraper2.get(link, allow_redirects=False)
    if html_text2.status_code == 200:
        player_data_soup = BeautifulSoup(html_text2.text, 'html.parser')
        info = player_data_soup.find_all('div', class_= 'row cf mt05e w100')
        try:
            postion = info[0].find_all('span', class_='semi-bold')[0].text
            #print(info[1].find_all('span', class_='semi-bold'))
            salary = info[1].find_all('span', class_='semi-bold')[-1].text
            results.append([team_name, name, postion, salary, link])
            
            # PREM STATS ONLY
            # Issue: prem isnt the top for all players, so we need to find the w100 div associatd to prem only
            try:
                stats = player_data_soup.find_all('div', class_='grid-item has-indicator overview pr')
                # we can use goals to get the minutes and in turn, the minutes to get the assits
                
                goals = stats[0].find('div', class_='stat-text').text
                goalsPer90 = stats[0].find('div', class_='stat-strong').text  
                assistsPer90 = stats[1].find('div', class_='stat-strong').text   
                xGPer90 = stats[3].find('div', class_='stat-strong').text
                xAPer90 = player_data_soup.find_all('div', class_='invisible540 grid-item has-indicator overview pr')[0].find('div', class_='stat-strong').text               
                print(f"{name}'s Goals: {goals}, Goals per 90: {goalsPer90}, Assists per 90: {assistsPer90}, xG per 90: {xGPer90}, xA per 90: {xAPer90}")
                
                # goalsPer90 = stats[0].find_all('div', class_='')[1].find('p').text    
                # assistsPer90 = stats[0].find_all('div', class_='col-lg-1')[2].find('p').text    
                # minutes = stats[0].find_all('div', class_='col-lg-2')[0].find('p').text
            except IndexError:
                pass     
        
        except IndexError:
            print(f"{link}")
            pass
        
        
    
    else:
        pass

# with open('FootystatsDatabase.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Club Name", "Player Name", "Position", "Salary", "FootyStats Link"])
#     writer.writerow(results)

print(0xd)        


#Using pandas
array = np.array(results)
df = pd.DataFrame({'Club Name': array[:, 0], 'Player Name': array[:, 1], 'Position': array[:, 2], 'Salary': array[:, 3], 'FootyStats Link': array[:, 4]})
df = df[df['Salary'].str.contains("€")]
df.to_csv("Database/FootystatsDatabase.csv", index=False, na_rep='Unknown')


    
    
    





    
# for team in teams:
#     link = team.find('a')['href']
#     print(link)
#     team_name = team.find('a').text
#     print(team_name)



