from Player import Player
from Deck import Deck
from CardLine import CardLine

class Game(object):
  total_wealth = 1010
  # Initializes players.
  # Determine who wins. (Note: pg. 7 of rules: "In the case of a tie, the tied players share victory.")

  def __init__(self, num_players):
    self.players = [Player()]*num_players
    self.deck = Deck().new(num_players)
    self.cardline = CardLine()
