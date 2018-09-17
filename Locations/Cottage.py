from Location import Location

class Cottage(Location):

  def __init__(self, workers=0, side=Location.SIDE_A):
    super(Cottage, self).__init__(workers, side, 12, 12)