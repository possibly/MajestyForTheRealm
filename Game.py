from Player import Player
from Deck import Deck
from Display import Display

class Game(object):
  # Determine who wins. (Note: pg. 7 of rules: "In the case of a tie, the tied players share victory.")
  total_wealth = 1010
  standard_draw = 6

  def __init__(self, **kwargs):
    self.names = kwargs.get('names', [1,2,3,4])
    self.display = kwargs.get('display', Display())
    self.deck = kwargs.get('deck', Deck.new(len(self.names)))
    self.players = kwargs.get('players', [Player(name=n) for n in self.names])
    self.current_player_index = kwargs.get('current_player_index', 0)
    self.picked_cards = kwargs.get('picked_cards', [])

  def copy(self, **kwargs):
    return Game(
      names = kwargs.get('names', self.names),
      display = kwargs.get('display', self.display),
      deck = kwargs.get('deck', self.deck),
      players = kwargs.get('players', self.players),
      current_player_index = kwargs.get('current_player_index', self.current_player_index),
      picked_cards = kwargs.get('picked_cards', self.picked_cards)
    )

  def current_player(self):
    return self.players[self.current_player_index]

  def draw(self, draw_number):
    # Draws Cards from the Deck and onto the Display.
    deck, cards = self.deck.draw(draw_number)
    return self.copy (
      display = Display.add(self.display, cards),
      deck = deck,
    )

  def pick(self, position):
    # Picks a Card from the Display and gives it to the current Player.
    display, picked_card = self.display.pick(position)
    deck, drawn_cards = self.deck.draw(1)
    return self.copy (
      display = Display.add(display, drawn_cards),
      deck = deck,
      players = [p.give(picked_card) if self.current_player() == p else p for p in self.players],
      picked_cards = self.picked_cards.push(picked_card)
    )

  def score(self):
    return self.copy (
      players = [p.score(self.picked_cards[-1]) if self.current_player() == p else p.score_other(self.picked_cards[-1]) for p in self.players],
    )

  def next_turn(self):
    next_index = self.current_player_index + 1
    if next_index >= len(self.players):
      next_index = 0
    return self.copy (
      current_player_index = next_index,
    )
