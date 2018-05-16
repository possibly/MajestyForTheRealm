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

  def score_value(self):
    if side == 'A':
      return value_a
    else:
      return value_b

class Mill(Location):
  name = 'Mill'
  value_a = 10

  def __init__(self, workers=0, side='A'):
    super(Mill, self).__init__(workers, side)

  def score(self):
    return {'wealth': (lambda owner: self.workers * 2), 'meeples': (lambda owner: 0), 'other': (lambda player: 0)}

class Brewery(Location):
  name = 'Brewery'
  value_a = 11

  def __init__(self, workers=0, side='A'):
    super(Brewery, self).__init__(workers, side)

  def score(self):
    return {'wealth': (lambda owner: self.workers * 2), 'meeples': (lambda owner: self.workers), 'other': _other_score_a}

  def _other_score_a(self, player):
    if player.locations[Mill.name].workers > 0:
      return 2
    else:
      return 0

class Cottage(Location):
  name = 'Cottage'
  value_a = 12

  def __init__(self, workers=0, side='A'):
    super(Cottage, self).__init__(workers, side)

  def score(self):
    return {'wealth': _owner_score_a, 'meeples': (lambda owner: 0), 'other': (lambda player: 0)}

  def _owner_score_a(self, owner):
    return (owner.locations[Mill.name].workers + owner.locations[Brewery.name].workers + self.workers) * 2

class Guardhouse(Location):
  name = 'Guardhouse'
  value_a = 13

  def __init__(self, workers=0, side='A'):
    super(Guardhouse, self).__init__(workers, side)

  def score(self):
    return {'wealth': _owner_score_a, 'meeples': (lambda owner: 0), 'other': (lambda player: 0)}

  def _owner_score_a(self, owner):
    return (owner.locations[Barracks.name].workers + owner.locations[Inn.name].workers + self.workers) * 2

class Barracks(Location):
  name = 'Barracks'
  value_a = 14

  def __init__(self, workers=0, side='A'):
    super(Barracks, self).__init__(workers, side)

  def score(self):
    return {'wealth': (lambda owner: self.workers * 3), 'meeples': (lambda owner: 0), 'other': (lambda player: 0)}

class Inn(Location):
  name = 'Inn'
  value_a = 15

  def __init__(self, workers=0, side='A'):
    super(Inn, self).__init__(workers, side)

  def score(self):
    return {'wealth': (lambda owner: self.workers * 4), 'meeples': (lambda owner: 0), 'other': _other_score_a}

  def _other_score_a(self, player):
    if player.locations[Brewery.name].workers > 0:
      return 3
    else:
      return 0

class Castle(Location):
  name = 'Castle'
  value_a = 16

  def __init__(self, workers=0, side='A'):
    super(Castle, self).__init__(workers, side)

  def score(self):
    return {'wealth': (lambda owner: self.workers * 5), 'meeples': (lambda owner: self.workers), 'other': (lambda player: 0)}

class Infirmary(Location):
  name = 'Infirmary'
  value_a = 0

  def __init__(self, workers=0, side='A'):
    super(Infirmary, self).__init__(workers, side)

  def score(self):
    return {'wealth': (lambda owner: self.workers * -1), 'meeples': (lambda owner: 0), 'other': (lambda player: 0)}
