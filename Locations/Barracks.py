from Location import Location

class Barracks(Location):

  def __init__(self, workers=0, side=Location.SIDE_A):
  	super(Barracks, self).__init__(workers, side, 14, 8)
