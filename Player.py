from Locations import *

class Player(object):
  def __init__(self, locations_sides, starting_wealth=0, starting_meeples=5):
    # locations_sides is an array of length 8 and either 'A' or 'B' in each index.
    self.locations = {
      Mill.name: Mill(side=locations_sides[0]),
      Brewery.name: Brewery(side=locations_sides[1]),
      Cottage.name: Cottage(side=locations_sides[2]),
      Guardhouse.name: Guardhouse(side=locations_sides[3]),
      Barracks.name: Barracks(side=locations_sides[4]),
      Inn.name: Inn(side=locations_sides[5]),
      Castle.name: Castle(side=locations_sides[6]),
      Infirmary.name: Infirmary(side=locations_sides[7])
    }
    self.wealth = starting_wealth
    self.meeples = starting_meeples

  def occupied_locations(self):
    # Does not include the Infirmary.
    return filter((lambda location: location.workers > 0 and location.name != Infirmary.name), self.locations.values())

  def total_workers(self):
    # Includes the Infirmary.
    workers_per_location = map((lambda location: location.workers), self.locations.values())
    return reduce((lambda workers, sum: workers + sum), workers_per_location)

  def send_worker_to_infirmary(self, location):
    self.locations[location].removeWorker()
    self.locations[Infirmary.name].addWorker()

  def gain_worker_from_infirmary(self):
    location_name = self.locations[Infirmary.name].removeWorker()
    self.locations[location_name].addWorker()