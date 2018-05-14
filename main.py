from Majesty import *

g = Game(4)
print g.players
print g.players[0].locations

all_players_location_names = map(lambda p: p.locations.keys(), g.players)
print all_players_location_names
