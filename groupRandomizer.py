from random import shuffle

playerAmount = int(input('How many players? '))
group = []

for i in range(playerAmount):
    playerName = str(input('Enter Player Name: '.format(i+1)))
    group.append(playerName)

shuffle(group)

teamSize = int(playerAmount/2)

team1 = group[:teamSize]
team2 = group[teamSize:]

print('\nTeam 1 is:\n {}\n'.format(team1), '\nTeam 2 is:\n {}'.format(team2))