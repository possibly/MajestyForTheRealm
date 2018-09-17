from Locations.Barracks import Barracks
from Locations.Brewery import Brewery
from Locations.Castle import Castle
from Locations.Cottage import Cottage
from Locations.Guardhouse import Guardhouse
from Locations.Infirmary import Infirmary
from Locations.Inn import Inn
from Locations.Mill import Mill
from Locations.Location import Location

DEFAULT_START_LOCATIONS = [Mill(), Brewery(), Cottage(), Guardhouse(), Barracks(), Inn(), Castle()]

class Player(object):
  def __init__(self, locations=DEFAULT_START_LOCATIONS, wealth=0, meeples=5):
    self.locations = locations
    self.wealth = wealth
    self.meeples = meeples
    self.locations_hash = {}
    for l in self.locations:
      self.locations_hash[l.__name__] = l

  def copy(self, locations):
    Player(locations, self.wealth, self.meeples)

  def location_names(self):
    map(Location.name, self.locations)
