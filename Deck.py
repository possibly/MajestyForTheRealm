from random import shuffle
from CardSets.TierOne import TierOne
from CardSets.TierTwo import TierTwo

class Deck(object):
  def __init__(self, cards=[]):
    self.cards = cards

  def new(self, num_players):
    return Deck(self._new_game_cards(num_players))

  def _new_game_cards(self, num_players):
    tier_one_cards = TierOne().cards()
    tier_two_cards = TierTwo().cards()
    shuffle(tier_one_cards)
    shuffle(tier_two_cards)
    if num_players == 2:
      tier_one_cards = tier_one_cards[0:6]
    elif num_players == 3:
      tier_one_cards = tier_one_cards[0:14]
    else:
      tier_one_cards = tier_one_cards[0:26]
    return tier_two_cards + tier_one_cards

  def draw(self, num=1):
    drawn = self.cards[0:num]
    not_drawn = self.cards[num:]
    return {'deck': Deck(not_drawn), 'cards': drawn}
