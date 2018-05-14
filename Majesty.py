from Locations import *

total_wealth = 1010
location_order = [Mill.name, Brewery.name, Cottage.name, Guardhouse.name, Barracks.name, Inn.name, Castle.name]

class Player(object):

  def __init__(self, id, locations_sides, starting_wealth=0, starting_meeples=5):
    # locations_sides is an array of length 8 and either 'A' or 'B' in each index.
    self.id = id
    self.locations = {
      Mill.name: Mill(side=locations_sides[0]),
      Brewery.name: Brewery(side=locations_sides[1]),
      Cottage.name: Cottage(side=locations_sides[2]),
      Guardhouse.name: Cottage(side=locations_sides[3]),
      Barracks.name: Barracks(side=locations_sides[4]),
      Inn.name: Inn(side=locations_sides[5]),
      Castle.name: Castle(side=locations_sides[6]),
      Infirmary.name: Infirmary(side=locations_sides[7])
    }
    self.wealth = starting_wealth
    self.meeples = starting_meeples

  def score_location(self, location_name, other_players):
    self.locations[location_name].addWorker()
    score = self.locations[location_name].score()
    self.wealth += score['wealth'](self)
    self.meeples += score['meeples'](self)
    for other_player in other_players:
      other_player.wealth += score['other'](other_player)
    return self.wealth

  def score_final(self):
    self.wealth += self.locations[Infirmary.name].score().wealth
    self.score_variety()
    self.score_majority()
    return self.wealth

  def score_infirmary(self):
    self.wealth -= self.locations[Infirmary.name].workers
    return self.wealth

  def score_variety(self):
    num_occupied_locations = len(_occupied_locations())
    self.wealth += num_occupied_locations*num_occupied_locations
    return self.wealth

  def _occupied_locations(self):
    # Does not include the Infirmary.
    return filter((lambda location: location.workers > 0 and location.name != Infirmary.name), self.locations.values())

  def _total_workers(self):
    # Includes the Infirmary.
    workers_per_location = map((lambda location: location.workers), self.locations.values())
    return reduce((lambda workers, sum: workers + sum), workers_per_location)

class Game(object):
  # Create the deck (shuffle, appropriate number of cards based on players)
  # Initializes players.
  # Determine who wins. (Note: pg. 7 of rules: "In the case of a tie, the tied players share victory.")

  def __init__(self, num_players):
    self.players = []
    for i in range(0, num_players):
      self.players.append(Player(i, ['a', 'a', 'a', 'a', 'a', 'a' ,'a', 'a']))

  # def score_majority():
    # for each player
      # Get their mills
      # Give just the player with the highest mill, points.


