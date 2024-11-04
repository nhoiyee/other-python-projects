
"""
open the csv file called "nfl_offensive_stats.csv" and
read in the csv data from the file
"""
# import the csv module
import csv
# open the csv file
with open('nfl_offensive_stats.csv', 'r') as f:
    # read the csv data
    data = list(csv.reader(f))
"""
the 3rd column in data is player position, the fourth column
is the player, and the 8th column is the passing yards.
For each player whose position in column 3 is "QB",
determine the sum of yards from column 8
"""
# create a dictionary to hold the player name and passing yards
passing_yards = {}
# loop through the data
for row in data:
    # check if the player is a quarterback
    if row[2] == 'QB':
        # check if the player is already in the dictionary
        if row[3] in passing_yards:
            # add the passing yards to the existing value
            passing_yards[row[3]] += int(row[7])
        else:
            # add the player to the dictionary
            passing_yards[row[3]] = int(row[7])
"""
sort the players by the sum of passing yards
"""
# sort the dictionary by passing yards in descending order
sorted_passing_yards = {k: v for k, v in sorted(passing_yards.items(), key=lambda item: item[1], reverse=True)}
"""
print the sum of the passing yards sorted by sum
of passing yards in descending order
Do not include Tom Brady because he wins too much
"""
# loop through the sorted dictionary
for player, yards in sorted_passing_yards.items():
    # check if the player is Tom Brady
    if player != 'Tom Brady':
        # print the player and passing yards
        print(f'{player}: {yards} passing yards')


import matplotlib.pyplot as plt
import numpy as np
"""
create a scatter plot of the players by their number of passing yards
only for players with more than 4000 passing yards
"""
# create a list of players and passing yards with more than 4000 yards
players = [player for player, yards in sorted_passing_yards.items() if yards > 4000]
yards = [yards for player, yards in sorted_passing_yards.items() if yards > 4000]
# create a scatter plot of the players and passing yards
plt.scatter(players, yards)
plt.xticks(rotation=90)
plt.show()


