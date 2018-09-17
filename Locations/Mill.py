from Location import Location

class Mill(Location):

  def __init__(self, workers=0, side=Location.SIDE_A):
    super(Mill, self).__init__(workers, side, 10, 14)
