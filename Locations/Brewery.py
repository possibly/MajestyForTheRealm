from Location import Location

class Brewery(Location):

  def __init__(self, workers=0, side=Location.SIDE_A):
    super(Brewery, self).__init__(workers, side, 11, 12)
