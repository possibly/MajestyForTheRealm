class Location(object):
  SIDE_A = 'A'
  SIDE_B = 'B'

  def __init__(self, workers, side, value_a, value_b):
    self.workers = workers
    self.side = side
    self.value_a = value_a
    self.value_b = value_b

  def value(self):
    if self.side == SIDE_A:
      return self.value_a
    else:
      return self.value_b

  @classmethod
  def sum_workers(cls, locationA, locationB):
    return locationA.workers + locationB.workers

  @classmethod
  def name(cls, location):
    location.__class__.__name__
