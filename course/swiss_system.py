import json

with open('./data/players.json', 'r') as file:
    players = json.load(file)

# Tri des joueurs par points d'elo
players_sorted = sorted(players, key=lambda player: player['elo_points'])

players_count = len(players_sorted)
players_s1 = players_sorted[0:players_count//2]
players_s2 = players_sorted[players_count//2:players_count]

versus = []
for i in range(0, players_count//2):
    versus.append([players_s1[i], players_s2[i]])

with open("./data/versus.json", "w") as outfile:
    json.dump(versus, outfile, indent=4)