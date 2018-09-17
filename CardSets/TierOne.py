from CardSet import *

class TierOne(CardSet):

  def __init__(self):
    super(TierOne, self).__init__()
    self.Brewers = [Brewer()]*4
    self.Guards = [Guard()]*3
    self.Innkeepers = [Innkeeper()]*2
    self.InnkeeperGuards = [InnkeeperGuard()]
    self.InnkeeperKnights = [InnkeeperKnight()]
    self.InnkeeperQueens = [InnkeeperQueen()]
    self.Knights = [Knight()]*2
    self.Medics = [Medic()]*3
    self.MedicBrewers = [MedicBrewer()]
    self.MedicGuards = [MedicGuard()]
    self.Millers = [Miller()]*7
    self.MillerBrewers = [MillerBrewer()]
    self.MillerKnights = [MillerKnight()]
    self.Queens = [Queen()]*3
    self.QueenGuards = [QueenGuard()]

