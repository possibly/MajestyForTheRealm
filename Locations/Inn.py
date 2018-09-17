from Location import Location

class Inn(Location):

  def __init__(self, workers=0, side=Location.SIDE_A):
    super(Inn, self).__init__(workers, side, 15, 12)
