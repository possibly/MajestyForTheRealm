from Locations import *
from Player import *

total_wealth = 1010

def score_location(scorer, location_name, other_players):
  scorer.locations[location_name].score()
  wealth, meeples, other = self.locations[location_name].score().values()
  scorer.wealth += wealth(scorer)
  scorer.meeples += meeples(scorer)
  for other_player in other_players:
    other_player.wealth += other(other_player)

def score_final(players):
  for player in players:
    player.wealth += score_infirmary(player)
    player.wealth += score_variety(player)
  # Score Majority
  for location_name in location_order: # Player.location_order
    highest_player = players[0]
    for player in players:
      if player.locations[location_name].workers > highest_player.locations[location_name].workers:
        highest_player = player
    highest_player.wealth += highest_player.locations[location_name].score_value()

def score_infirmary(player):
  return player.locations[Infirmary.name].score().wealth(player)

def score_variety(player):
  return len(player.occupied_locations())*len(player.occupied_locations())

class Game(object):
  # Create the deck (shuffle, appropriate number of cards based on players)
  # Initializes players.
  # Determine who wins. (Note: pg. 7 of rules: "In the case of a tie, the tied players share victory.")

  def __init__(self, num_players):
    self.players = []
    for i in range(0, num_players):
      self.players.append(Player(['a', 'a', 'a', 'a', 'a', 'a' ,'a', 'a']))
