from bs4 import BeautifulSoup
import cloudscraper

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


scraper2 = cloudscraper.create_scraper(delay=15, browser="chrome")
for (_, _, link) in player_list:
    html_text2 = scraper2.get(link).text
    player_data_soup = BeautifulSoup(html_text2, 'html.parser')
    info = player_data_soup.find_all('div', class_= 'w100 row cf')
    # Need to collect salary and postion information for each player
    
    
    





    
# for team in teams:
#     link = team.find('a')['href']
#     print(link)
#     team_name = team.find('a').text
#     print(team_name)



