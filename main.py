from Majesty import *

g = Game(4)
print "A 4 player game object, g, has been initialized."
print "The player objects are: "
print ""
print g.players
print ""
print "The first player's location objects are:"
print ""
print g.players[0].locations
print ""
print "The location names of every player's locations are: "
all_players_location_names = map(lambda p: p.locations.keys(), g.players)
print ""
print all_players_location_names
print ""
print "The total amount of wealth available for ownership in the game is: " + str(total_wealth)
print ""
