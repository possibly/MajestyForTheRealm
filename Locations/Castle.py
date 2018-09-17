from Location import Location

class Castle(Location):

  def __init__(self, workers=0, side=Location.SIDE_A):
    super(Castle, self).__init__(workers, side, 16, 16)
