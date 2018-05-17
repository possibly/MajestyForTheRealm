from copy import deepcopy as dcopy

class Location(object):
  def __init__(self, workers=0, side='A'):
    self.workers = workers
    self.side = side

  def addWorker(self):
    self.workers += 1
    return self.workers

  def removeWorker(self):
    self.workers -= 1
    return self.workers

  def value(self):
    if self.side == 'A':
      return self.value_a
    else:
      return self.value_b

class Mill(Location):
  name = 'Mill'
  value_a = 10

  def __init__(self, workers=0, side='A'):
    super(Mill, self).__init__(workers, side)

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    s.wealth += self.workers*2
    return [s, other_players]

class Brewery(Location):
  name = 'Brewery'
  value_a = 11

  def __init__(self, workers=0, side='A'):
    super(Brewery, self).__init__(workers, side)

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    op = dcopy(other_players)
    s.wealth += self.workers * 2
    s.meeples += self.workers
    for other_player in op:
      if other_player.locations[Mill.name].workers > 0:
        other_player.wealth += 2
    return [s, op]

class Cottage(Location):
  name = 'Cottage'
  value_a = 12

  def __init__(self, workers=0, side='A'):
    super(Cottage, self).__init__(workers, side)

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    s.gain_worker_from_infirmary()
    s.wealth += (s.locations[Mill.name].workers + s.locations[Brewery.name].workers + self.workers) * 2
    return [s, other_players]

class Guardhouse(Location):
  name = 'Guardhouse'
  value_a = 13

  def __init__(self, workers=0, side='A'):
    super(Guardhouse, self).__init__(workers, side)

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    s.wealth += (owner.locations[Barracks.name].workers + owner.locations[Inn.name].workers + self.workers) * 2
    return [s, other_players]

class Barracks(Location):
  name = 'Barracks'
  value_a = 14

  def __init__(self, workers=0, side='A'):
    super(Barracks, self).__init__(workers, side)

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    op = dcopy(other_players)
    s.wealth += self.workers * 3
    for other_player in op:
      if other_player.locations[Guardhouse.name].workers < self.workers:
        for location_name in location_order:
          if other_player.locations[location_name].workers > 0:
            other_player.send_worker_to_infirmary()
            break
    return [s, op]

class Inn(Location):
  name = 'Inn'
  value_a = 15

  def __init__(self, workers=0, side='A'):
    super(Inn, self).__init__(workers, side)

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    op = dcopy(other_players)
    s.wealth += self.workers * 4
    for other_player in op:
      if other_player.locations[Brewery.name].workers > 0:
        other_player.wealth += 3
    return [s, op]

class Castle(Location):
  name = 'Castle'
  value_a = 16

  def __init__(self, workers=0, side='A'):
    super(Castle, self).__init__(workers, side)

  def score(self, scorer, other_players):
    s = dcopy(scorer)
    s.wealth += self.workers * 5
    s.meeples += self.workers
    return [s, other_players]

class Infirmary(Location):
  name = 'Infirmary'
  value_a = 0
  stack = []

  def __init__(self, workers=0, side='A'):
    super(Infirmary, self).__init__(workers, side)

  def addWorker(self, location):
    self.worker += 1
    stack.append(location.name)

  def removeWorker(self):
    self.worker -= 1
    return stack.pop()

location_order = [Mill.name, Brewery.name, Cottage.name, Guardhouse.name, Barracks.name, Inn.name, Castle.name]