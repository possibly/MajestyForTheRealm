from copy import deepcopy as dcopy
from Constants import *

class Location(object):
  def __init__(self, workers=0, side=SIDE_A):
    self.workers = workers
    self.side = side

  def addWorker(self):
    self.workers += 1
    return self.workers

  def removeWorker(self):
    self.workers -= 1
    return self.workers

  def value(self):
    if self.side == SIDE_A:
      return self.value_a
    else:
      return self.value_b

class Mill(Location):
  value_a = 10

  def __init__(self):
    super(Mill, self).__init__()

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    s.wealth += self.workers*2
    return [s, other_players]

class Brewery(Location):
  value_a = 11

  def __init__(self):
    super(Brewery, self).__init__()

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    op = dcopy(other_players)
    s.wealth += self.workers * 2
    s.meeples += self.workers
    for other_player in op:
      if other_player[MILL].workers > 0:
        other_player.wealth += 2
    return [s, op]

class Cottage(Location):
  value_a = 12

  def __init__(self):
    super(Cottage, self).__init__()

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    s.gain_worker_from_infirmary()
    s.wealth += (s[MILL].workers + s[BREWERY].workers + self.workers) * 2
    return [s, other_players]

class Guardhouse(Location):
  value_a = 13

  def __init__(self):
    super(Guardhouse, self).__init__()

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    s.wealth += (s[BARRACKS].workers + s[INN].workers + self.workers) * 2
    return [s, other_players]

class Barracks(Location):
  value_a = 14

  def __init__(self):
    super(Barracks, self).__init__()

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    op = dcopy(other_players)
    s.wealth += self.workers * 3
    for other_player in op:
      if other_player[GUARDHOUSE].workers < self.workers:
        for location_name in location_order:
          if other_player[location_name].workers > 0:
            other_player.send_worker_to_infirmary()
            break
    return [s, op]

class Inn(Location):
  value_a = 15

  def __init__(self):
    super(Inn, self).__init__()

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    op = dcopy(other_players)
    s.wealth += self.workers * 4
    for other_player in op:
      if other_player[BREWERY].workers > 0:
        other_player.wealth += 3
    return [s, op]

class Castle(Location):
  value_a = 16

  def __init__(self):
    super(Castle, self).__init__()

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    s.wealth += self.workers * 5
    s.meeples += self.workers
    return [s, other_players]

class Infirmary(Location):
  value_a = 0
  stack = []

  def __init__(self):
    super(Infirmary, self).__init__()

  def addWorker(self, location):
    self.worker += 1
    stack.append(location.name)

  def removeWorker(self):
    self.worker -= 1
    return stack.pop()
