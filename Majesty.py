from Player import *

total_wealth = 1010

class Game(object):
  # Initializes players.
  # Determine who wins. (Note: pg. 7 of rules: "In the case of a tie, the tied players share victory.")

  def __init__(self, num_players):
    self.players = []
    for i in range(0, num_players):
      self.players.append(Player())
