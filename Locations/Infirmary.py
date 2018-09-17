from Location import Location

class Infirmary(Location):

  def __init__(self, workers=0, side=Location.SIDE_A):
    super(Infirmary, self).__init__(workers, side, 0, -10)