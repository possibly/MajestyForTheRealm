from Location import Location

class Guardhouse(Location):

  def __init__(self, workers=0, side=Location.SIDE_A):
    super(Guardhouse, self).__init__(workers, side, 13, 8)