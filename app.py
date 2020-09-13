import constants
import copy
    
def clean_data(players):
    for player in players:
        player['height'] = int(player['height'].split()[0])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
                    
def balance_teams():
    team_panthers.extend(players_copy[0:6])
    team_bandits.extend(players_copy[6:12])
    team_warriors.extend(players_copy[12:])
    
def player_names(team):
    for players in team:
        names = players['name']
        print(names)  
                
def print_team_stats():
    print('Teams:\n1) Panthers\n2) Bandits\n3) Warriors')
    while True:
        try:
            team_input = input('Please enter your team: ')
            if team_input != '1' and team_input != '2' and team_input != '3':
                raise ValueError
        except ValueError as err:
                print('Please enter 1, 2, or 3')
                print(err)
        if team_input == '1':
            print('\n')
            print('Team Panther Stats:\n======\nTotal Players:{} '.format(len(team_panthers)))
            print('\n')
            print('Players on Team:')
            player_names(team_panthers)
            print('\n')
            input('Please press Enter to continue...')
        elif team_input == '2':
            print('\n')
            print('Team Bandits Stats:\n======\nTotal Players:{} '.format(len(team_bandits)))
            print('\n')
            print('Players on Team:')
            print('\n')
            player_names(team_bandits)
            print('\n')
            input('Please press Enter to continue...')
        elif team_input == '3':
            print('\n')
            print('Team Warriors Stats:\n======\nTotal Players:{} '.format(len(team_warriors)))
            print('\n')
            print('Players on Team:')
            print('\n')
            player_names(team_warriors)
            print('\n')
            input('Please press Enter to continue...')
            
def main():
    print('BASKETBALL TEAM STATS TOOL\n\n----MENU----\n\nHere are your choices:\n\n1) Display Team Stats\n2) Quit')
    print('\n')
    while True:
        try:
            menu_input = input('Please enter your selection: ')
            if menu_input != '1' and menu_input != '2':
                raise ValueError
        except ValueError as err:
            print ('Please enter 1 or 2...')
        if menu_input == '1':
            print_team_stats()
        elif menu_input == '2':
            print('==========\nThank you! Have a great day!')
            break  
                
team_panthers = []
team_bandits = []
team_warriors = []
teams_copy = copy.deepcopy(constants.TEAMS)
players_copy = copy.deepcopy(constants.PLAYERS)
num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)

clean_data(players_copy)
balance_teams()

if __name__ == '__main__':
    main()

      

    
    