from random import shuffle

group = [input('Enter player 1 '), input('Enter player 2 '), input('Enter player 3 '), input('Enter player 4 '), input('Enter player 5 '), input('Enter player 6 '), input('Enter player 7 '), input('Enter player 8 ')]

shuffle(group)

print('Team 1 is: ')
print(group[0])
print(group[1])
print(group[2])
print(group[3])

print('Team 2 is: ')
print(group[4])
print(group[5])
print(group[6])
print(group[7])
