from Locations import *
from Constants import *

class Player(object):
  def __init__(self, sides=[SIDE_A,SIDE_A,SIDE_A,SIDE_A,SIDE_A,SIDE_A,SIDE_A,SIDE_A], 
                     order=[MILL, BREWERY, COTTAGE, GUARDHOUSE, BARRACKS, INN, CASTLE], 
                     starting_wealth=0, 
                     starting_meeples=5):
    self[MILL] = Mill(side=sides[0])
    self[BREWERY] = Brewery(side=sides[1])
    self[COTTAGE] = Cottage(side=sides[2])
    self[GUARDHOUSE] = Guardhouse(side=sides[3])
    self[BARRACKS] = Barracks(side=sides[4])
    self[INN] = Inn(side=sides[5])
    self[CASTLE] = Castle(side=sides[6])
    self[INFIRMARY] = Infirmary(side=sides[7])
    self.order = order
    self.wealth = starting_wealth
    self.meeples = starting_meeples

  def __getitem__(self, key):
    return getattr(self, key)

  def __setitem__(self, key, value):
    return setattr(self, key, value)

  def occupied_locations(self):
    # Does not include the Infirmary.
    return filter((lambda l_name: self[lname].workers > 0), self.order)

  def send_worker_to_infirmary(self, location_name):
    self[location_name].removeWorker()
    self[INFIRMARY].addWorker()

  def gain_worker_from_infirmary(self):
    location_name = self[INFIRMARY].removeWorker()
    self[location_name].addWorker()

  def score(self, location_name, other_players):
    return self[location_name].score(self, other_players)

  def addWorker(self, location_name):
    return self[location_name].addWorker()
