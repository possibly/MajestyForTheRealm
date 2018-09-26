from Locations.Realm import Realm

class Player(object):
  def __init__(self, **kwargs):
    self.wealth = kwargs.get('wealth', 0)
    self.name = kwargs.get('name', '')
    self.realm = kwargs.get(Realm.__name__, Realm())
    self.meeples = kwargs.get('meeples', 0)

  def __eq__(self, other):
    return self.name == other.name

  def __repr__(self):
    return 'Player ' + str(self.name)

  def copy(self, **kwargs):
    return Player (
      wealth = kwargs.get('wealth', self.wealth),
      name = kwargs.get('name', self.name),
      realm = kwargs.get(Realm.__name__, self.realm),
      meeples = kwargs.get('meeples', self.meeples)
    )

  def give(self, card):
    return self.copy (
      realm = self.realm.replace(self.realm.get(card).add_card(card))
    )

  def add_wealth(self, num):
    return self.copy (
      wealth = self.wealth + num
    )

  def add_meeples(self, num):
    if self.meeples + num > 5:
      return self.copy (
        meeples = 5
      )
    return self.copy (
      meeples = self.meeples + num
    )

  def score(self, card):
    return self.realm.get(card).score(self)

  def score_other(self, card):
    return self.realm.get(card).score_other(self)

  def _heal(self):
    if len(self.realm.Infirmary.cards) == 0:
      return self
    else:
      card, new_infirmary = self.realm.Infirmary.pop_card()
      new_loc = self.realm.get(card).add_card(card)
      return self.copy (
        realm = self.realm.replace(new_infirmary, new_loc)
      )

  def _attacked(self, num_knights):
    if len(self.realm.Guardhouse.cards) > num_knights:
      return self
    for l in self.realm.locations:
      if len(l.cards) > 0:
        card, popped_l = l.pop_card()
        added_to_l = self.realm.get(card).add_card(card)
        return self.copy(
          realm = self.realm.repalce(popped_l, add_to_l)
        )
