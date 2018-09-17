from CardSet import *

class TierTwo(CardSet):

  def __init__(self):
    super(TierTwo, self).__init__()
    self.Brewers = [Brewer()]*2
    self.Guards = [Guard()]*2
    self.Innkeepers = [Innkeeper()]*2
    self.InnkeeperKnights = [InnkeeperKnight(), InnkeeperKnight()]
    self.InnkeeperMedics = [InnkeeperMedic()]
    self.InnkeeperQueens = [InnkeeperQueen()]
    self.Knights = [Knight()]
    self.KnightBrewers = [KnightBrewer()]
    self.KnightGuards = [KnightGuard(), KnightGuard()]
    self.Medics = [Medic()]*2
    self.MedicBrewers = [MedicBrewer(), MedicBrewer()]
    self.MedicGuards = [MedicGuard(), MedicGuard()]
    self.Millers = [Miller()]*2
    self.MillerBrewers = [MillerBrewer()]
    self.MillerKnights = [MillerKnights()]
    self.Queens = [Queen()]*2
    self.QueenMedics = [QueenMedic()]
