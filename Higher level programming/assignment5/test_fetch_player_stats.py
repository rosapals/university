from fetch_player_statistics import extract_teams
from fetch_player_statistics import extract_players
from fetch_player_statistics import extract_player_statistics
from fetch_player_statistics import extract_top_players
from nba_plot import draw_plot

# This file tests all functions for task 5.5

def run_all_tests():
    # run_all_tests is the main function and runs all subtests

    url = 'https://en.wikipedia.org/wiki/2021_NBA_playoffs'
    teams = test_extract_teams(url)

    top_three_per_team = {}
    for t in teams:
        url = teams[t]
        players = test_extract_players(url)

        players_stats = {}
        for p in players:
            url = players[p]
            stats = test_extract_player_statistics(url)
            players_stats[p] = stats
        # find top three players of a team based on ppg
        top_players = extract_top_players(players_stats)

        # store top players of each team
        top_three_per_team[t] = top_players

    # make plots based on top three players per team
    test_nba_plot(top_three_per_team)



# Tests below are called from run_all_tests()

def test_extract_teams(url):
    """Tests function extract_teams in fetch_player_statistics.py
    Input
        url (str): NBA wiki site
    Returns
        teams (dict): Dictionary of all teams found, on the form { 'team name' : 'wiki site' }
    """
    teams = extract_teams(url)
    assert teams == {
                    'Milwaukee': r'https://en.wikipedia.org/wiki/2020%E2%80%9321_Milwaukee_Bucks_season', 
                    'Brooklyn': r'https://en.wikipedia.org/wiki/2020%E2%80%9321_Brooklyn_Nets_season', 
                    'Philadelphia': r'https://en.wikipedia.org/wiki/2020%E2%80%9321_Philadelphia_76ers_season', 
                    'Phoenix': r'https://en.wikipedia.org/wiki/2020%E2%80%9321_Phoenix_Suns_season', 
                    'LA Clippers': r'https://en.wikipedia.org/wiki/2020%E2%80%9321_Los_Angeles_Clippers_season', 
                    'Atlanta': r'https://en.wikipedia.org/wiki/2020%E2%80%9321_Atlanta_Hawks_season', 
                    'Utah': r'https://en.wikipedia.org/wiki/2020%E2%80%9321_Utah_Jazz_season', 
                    'Denver': r'https://en.wikipedia.org/wiki/2020%E2%80%9321_Denver_Nuggets_season'
                    }
    return teams

def test_extract_players(url):
    """Tests function extract_players in fetch_player_statistics.py
    Input
        url (str): NBA team's wiki site
    Returns
        players (dict): Dictionary of all team players found, on the form { 'name' : 'player's wiki site' }
    """
    return extract_players(url)

def test_extract_player_statistics(url):
    """Tests function extract_player_statistics in fetch_player_statistics.py
    Input
        url (str): NBA players's wiki site
    Returns
        scores (list of floats): List containing the players ppg, bpg and rpg
    """
    return extract_player_statistics(url)

def test_nba_plot(top_three_per_team):
    """Test plot drawing skills of draw_plot() function in nba_plot
    Input
        top_three_per_team (dict): The three top players based on point per game (ppg)
    """
    draw_plot(top_three_per_team)

run_all_tests()