from bs4 import BeautifulSoup
import re
from requesting_urls import get_html
from filter_urls import find_articles
from filter_urls import list_to_str

def extract_teams(url):
    """Given an NBA url, extract teams playing in semifinal
    Inputs
        url (str): Url of wikipedia website
    Returns
        teams (hashmap): HashMap with team name as key, and team 
                        url as value
    """
    # request html
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")

    # find the bracket
    bracket_header = soup.find(id="Bracket")
    bracket = bracket_header.find_next("table")
    rows = bracket.find_all("tr")

    team_names = []
    urls = []
    teams = {}

    # iterate rows in bracket
    for i in range (1, len(rows)):
        # fetch significant data from cells
        team_data = rows[i].find_all("td")
        # fetch team names from cells
        team_data_text = [team.get_text(strip=True) for team in team_data]
        # fetch team urls from cells
        team_data_url = extract_url(team_data)
     
        # Remove empty and unvalid cells
        team_names += [x for x in team_data_text if is_team_name(x)]
        urls += [x for x in team_data_url if x]
 
    # Remove teams not in semifinals
    team_names = filter_list(team_names)
    urls = filter_list(urls)
    
    # Create a dict on the form {team name : team url}
    for name in team_names:
        for part in name.split():
            for url in urls:
                if part in url:
                    teams[name] = url

    return teams

def filter_list(liste):
    """Returns a list only containing elements appearing more than
    once. Removes '*' character from element
    Input:
        liste (list of str): The list to filter
    Returns:
        filtered_list (list of str): Same list as input, filtered
    """
    filtered_list = [x.strip('*') for x in liste if (liste.count(x) > 1)]

    # remove duplicates
    filtered_list = list(set(filtered_list))
    return filtered_list

def is_team_name(streng):
    """Checks if a string is a basketball team's name
    Returns
        True if the string seems like a name, else
        False
    """
    return len(streng) > 2 

def extract_url(team_data):
    """Takes data cells and finds wiki articles
    Inputs
        team_data (<td> elements of a row in bracket): Data of a team
    Returns
        The <td> element(s) that contain(s) an url with wikipedia base url.
    """
    return find_articles(str(team_data), base="https://en.wikipedia.org")

def extract_players(team_url):
    """Takes a wiki site of a NBA team and finds team players
    and their wiki urls
    Input
        team_url (str): Url to a NBA team
    Returns
        players (dict): Dictionary of players on the form { 'player name' : 'player_url' }
    """

    #base_url = "https://en.wikipedia.org"
    html = get_html(team_url)
    soup = BeautifulSoup(html, "html.parser")
    roster_header = soup.find(id="Roster")
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")

    # hashmap to store player name and url
    players = {}

    # begin at row 4, to skip the header in the table
    for i in range(3, len(rows)):
        cells = rows[i].find_all("td")

        # extract readable text from cells
        cells_text = [cell.get_text(strip=True) for cell in cells]

        # fetch player name
        name = cells_text[2]

        # some names are saved with '(TW)' which is removed
        if name[-4:] == '(TW)':
            name = name[0:-4]

        # extracts all urls in table row
        found_urls = extract_url(cells)

        # extract the correct url
        player_url = found_urls[1]

        # save name and url
        players[name] = player_url
    return players

def extract_player_statistics(player_url):
    """Take a wiki url to a NBA player, and find cool stats
    Inputs
        player_url (str): Url to player's wiki site
    Returns
        score (list of floats): List of length 3, containing
                                [ppg, bpg, rpg]
    """
    ppg = 0.0 # points per game
    bpg = 0.0 # blocks per game
    rpg = 0.0 # rebounds per game
    scores = [ppg, bpg, rpg]

    html = get_html(player_url)
    soup = BeautifulSoup(html, "html.parser")

    # try to find table in different ways
    nba_header = soup.find(id="NBA_career_statistics")

    if nba_header is None:
        nba_header = soup.find(id="NBA")
    try:
        regular_season_header = nba_header.find_next(id="Regular_season")
        nba_table = regular_season_header.find_next("table")
    except:
        try:
            nba_table = nba_header.find_next("table")
        except:
            # give up on finding table
            return scores
    
    # find all rows in stats table
    rows = nba_table.find_all("tr")

    # find the row of season 2020-21
    found = False
    for row in rows:
        if not found:
            if '2020–21' in str(row):

                found = True

                row_data = row.find_all("td")
                # find the columns with relevant scores
                ppg = row_data[-1]
                bpg = row_data[-2]
                rpg = row_data[-5]

                # extract scores from cells
                ppg = ppg.text.strip()
                bpg = bpg.text.strip()
                rpg = rpg.text.strip()

    # store scores 
    scores = [ppg, bpg, rpg]

    # convert scores to float
    for i in range(3):
        try:
            scores[i] = float(scores[i])
        except ValueError:
            # if the score is not a number, set score to 0
            scores[i] = 0.0
    return scores

def extract_top_players(all_players):
    """Finds who are the top three players of the team based on points per game (ppg)
    Inputs
        all_players (dict): Dictionary on the form { 'player name' : [ppg, bpg, rpg] }
    Returns
        top three (dict): Dictionary of the top three players   {
                                                                'name' : 'Name Nameson',
                                                                'ppg'  : 0.0,
                                                                'bpg'  : 0.0,
                                                                'rpg'  : 0.0
                                                                }
    """
    # got the following code line from the internet, credit in README
    # sorts the dict of players based on ppg, high to low
    sorted_best_first = sorted(all_players.items(), key=lambda x: x[1], reverse=True)
    # we only care about the three best players
    sorted_best_first = sorted_best_first[0:3]

    # store collected data as shown in assignment text
    top_three = [None, None, None]
    for i in range(3):
        name  = sorted_best_first[i][0]
        scores = sorted_best_first[i][1]
        top_three[i] = {
                        'name' : name,
                        'ppg' : scores[0],
                        'bpg' : scores[1],
                        'rpg' : scores[2]
                        }
    return top_three