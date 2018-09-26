class Display(object):
  def __init__(self, cards=[]):
    if len(cards) > 6:
      raise ValueError('Cards was greater than 6 -- it must be less than or equal to 6!')
    self.cards = cards

  def pick(self, position):
    # position:int -- Natural numbers [1,2..6]
    if position <= 0 or position >= 7:
      raise ValueError('Picking a card takes natural numbers between 1..6')
    picked = self.cards[position-1]
    not_picked = self.cards[:position-1] + self.cards[position+1:]
    return [Display(not_picked), picked]

  @classmethod
  def add(cls, old_display, cards):
    return Display(old_display.cards + cards)
