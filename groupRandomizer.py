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

print('Team 1 is: ')
print(team1)
print('Team 2 is: ')
print(team2)