import matplotlib.pyplot as plt
import os

def draw_plot(teams):
    # Simply makes a plot for ppg, bpg and rpg
    # This code is super repetetive if you dont mind
    color_table =   {
                    'Milwaukee': "pink", 
                    'Brooklyn': "skyblue", 
                    'Philadelphia': "hotpink", 
                    'Phoenix': "purple", 
                    'LA Clippers': "linen", 
                    'Atlanta': "red", 
                    'Utah': "lightsalmon", 
                    'Denver': "orange"
                    }
    draw_ppg(teams, color_table)
    draw_bpg(teams, color_table)
    draw_rpg(teams, color_table)

def draw_ppg(teams, color_table):
    """Makes a plot over point per game,
    by top three player per team.
    Inputs:
        teams (dict): team name,
                    and name/stats of the top three player
        color_table (dict): Color chart
    """
    count = 0
    all_names = []

    # this code block makes a plot for ppg
    for team, players in teams.items():
        color = color_table[team]
        ppg = []
        bpg = []
        rpg = []
        names = []
        for p in players:
            names.append(p['name'])
            ppg.append(p['ppg'])
            #bpg.append(p['bpg'])
            #rpg.append(p['rpg'])
        all_names.extend(names)

        x = range(count, count + len(players))
        count += len(players)
        bars = plt.bar(x, ppg, color=color, label=team)
        plt.bar_label(bars)
    
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    plt.legend(loc=0)
    plt.grid(False)
    plt.title("POINTS PER GAME (top three players per team)")
    folder = 'NBA_player_statistics/'
    os.makedirs(folder, exist_ok=True)
    plt.savefig(folder+'players_over_ppg.png')
    plt.close()

def draw_bpg(teams, color_table):
    # this code block is similar to the one above,
    # but makes a plot for bpg instead of ppg. I copy the same code 
    # because I'm too stupid to think by myself
    count = 0
    all_names = []

    for team, players in teams.items():
        color = color_table[team]
        ppg = []
        bpg = []
        rpg = []
        names = []
        for p in players:
            names.append(p['name'])
            #ppg.append(p['ppg'])
            bpg.append(p['bpg'])
            #rpg.append(p['rpg'])
        all_names.extend(names)

        x = range(count, count + len(players))
        count += len(players)
        bars = plt.bar(x, bpg, color=color, label=team)
        plt.bar_label(bars)
    
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    plt.legend(loc=0)
    plt.grid(False)
    plt.title("BLOCKS PER GAME (top three players per team)")
    folder = 'NBA_player_statistics/'
    os.makedirs(folder, exist_ok=True)
    plt.savefig(folder+'players_over_bpg.png')
    plt.close()

def draw_rpg(teams, color_table):
    # this code block is similar to the one above,
    # but makes a plot for rpg instead of ppg. I copy the same code 
    # because I'm too stupid to think by myself
    count = 0
    all_names = []
    
    for team, players in teams.items():
        color = color_table[team]
        #ppg = []
        #bpg = []
        rpg = []
        names = []
        for p in players:
            names.append(p['name'])
            #ppg.append(p['ppg'])
            #bpg.append(p['bpg'])
            rpg.append(p['rpg'])
        all_names.extend(names)

        x = range(count, count + len(players))
        count += len(players)
        bars = plt.bar(x, rpg, color=color, label=team)
        plt.bar_label(bars)
    
    plt.xticks(range(len(all_names)), all_names, rotation=90)
    plt.legend(loc=0)
    plt.grid(False)
    plt.title("REBOUNDS PER GAME (top three players per team)")
    folder = 'NBA_player_statistics/'
    os.makedirs(folder, exist_ok=True)
    plt.savefig(folder+'players_over_rpg.png')
    plt.close()