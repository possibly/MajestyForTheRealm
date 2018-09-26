from Locations.Barracks import Barracks
from Locations.Brewery import Brewery
from Locations.Castle import Castle
from Locations.Cottage import Cottage
from Locations.Guardhouse import Guardhouse
from Locations.Infirmary import Infirmary
from Locations.Inn import Inn
from Locations.Mill import Mill

DEFAULT_ORDER = [
  Mill.__name__, 
  Brewery.__name__, 
  Cottage.__name__, 
  Guardhouse.__name__, 
  Barracks.__name__, 
  Inn.__name__, 
  Castle.__name__
]

class Realm(object):
  def __init__(self, **kwargs):
    self.Mill = kwargs.get(Mill.__name__, Mill())
    self.Brewery = kwargs.get(Brewery.__name__, Brewery())
    self.Cottage = kwargs.get(Cottage.__name__, Cottage())
    self.Guardhouse = kwargs.get(Guardhouse.__name__, Guardhouse())
    self.Barracks = kwargs.get(Barracks.__name__, Barracks())
    self.Inn = kwargs.get(Inn.__name__, Inn())
    self.Castle = kwargs.get(Castle.__name__, Castle())
    self.Infirmary = kwargs.get(Infirmary.__name__, Infirmary())
    self.order = kwargs.get('order', DEFAULT_ORDER)

  def replace(self, *args):
    kwargs = {}
    for l in args:
      kwargs[l.name] = l
    return Realm(
      Mill = kwargs.get(Mill.__name__, self.Mill),
      Brewery = kwargs.get(Brewery.__name__, self.Brewery),
      Cottage = kwargs.get(Cottage.__name__, self.Cottage),
      Guardhouse = kwargs.get(Guardhouse.__name__, self.Guardhouse),
      Barracks = kwargs.get(Barracks.__name__, self.Barracks),
      Inn = kwargs.get(Inn.__name__, self.Inn),
      Castle = kwargs.get(Castle.__name__, self.Castle),
      Infirmary = kwargs.get(Infirmary.__name__, self.Infirmary),
      order = kwargs.get('order', DEFAULT_ORDER)
    )

  def get(self, card):
    if card.chosen_location == None:
      raise ArgumentError('Please choose which location you would like to play this card at.')
    return getattr(self, card.chosen_location.__name__)

  def locations(self):
    x = []
    for name in self.order:
      x.push(getattr(self, name))
    return x
