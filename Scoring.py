from copy import deepcopy as dcopy

def score_final(players):
  p = dcopy(players)
  for player in p:
    player.wealth += score_infirmary(player)
    player.wealth += score_variety(player)
  return score_majority(p)

def score_infirmary(player):
  return player.locations[Infirmary.name].workers * -1

def score_variety(player):
  return len(player.occupied_locations())*len(player.occupied_locations())

def score_majority(players):
  players = dcopy(players)
  for location_name in location_order: # Locations.location_order
    highest_player = players[0]
    for player in players[1:]:
      if player.locations[location_name].workers > highest_player.locations[location_name].workers:
        highest_player = player
    highest_player.wealth += highest_player.locations[location_name].value()
  return players
