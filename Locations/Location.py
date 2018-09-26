from Cards.Card import Card

class Location(object):
  SIDE_A = 'A'
  SIDE_B = 'B'

  def __init__(self, cards, side, value_a, value_b):
    self.cards = cards
    self.side = side
    self.value_a = value_a
    self.value_b = value_b
    self.name = self.__class__.__name__

  def value(self):
    if self.side == SIDE_A:
      return self.value_a
    else:
      return self.value_b

  def add_card(self, card):
    cards = self.cards + [card]
    return self.__class__(cards, self.side)

  def pop_card(self):
    card = self.cards[0]
    new_loc = self.__class__(self.cards[1:], self.side)
    return [card, new_loc]

  def __eq__(self, other): 
    return self.name == other.name
