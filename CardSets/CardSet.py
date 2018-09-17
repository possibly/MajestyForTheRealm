from Cards.Brewer import Brewer
from Cards.Guard import Guard
from Cards.Innkeeper import Innkeeper
from Cards.InnkeeperGuard import InnkeeperGuard
from Cards.InnkeeperKnight import InnkeeperKnight
from Cards.InnkeeperMedic import InnkeeperMedic
from Cards.InnkeeperQueen import InnkeeperQueen
from Cards.Knight import Knight
from Cards.KnightBrewer import KnightBrewer
from Cards.KnightGuard import KnightGuard
from Cards.Medic import Medic
from Cards.MedicBrewer import MedicBrewer
from Cards.MedicGuard import MedicGuard
from Cards.Miller import Miller
from Cards.MillerBrewer import MillerBrewer
from Cards.MillerKnight import MillerKnight
from Cards.Queen import Queen
from Cards.QueenGuard import QueenGuard
from Cards.QueenMedic import QueenMedic

class CardSet(object):

  def __init__(self):
    self.Brewers = []
    self.Guards = []
    self.Innkeepers = []
    self.InnkeeperGuards = []
    self.InnkeeperKnights = []
    self.InnkeeperMedics = []
    self.InnkeeperQueens = []
    self.Knights = []
    self.KnightBrewers = []
    self.KnightGuards = []
    self.Medics = []
    self.MedicBrewers = []
    self.MedicGuards = []
    self.Millers = []
    self.MillerBrewers = []
    self.MillerKnights = []
    self.Queens = []
    self.QueenGuards = []
    self.QueenMedics = []

  def cards(self):
    return sum([getattr(self, key) for key in dir(self) if not key.startswith('__') and not key == 'cards'], [])
