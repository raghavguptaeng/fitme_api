import falcon
from water import Water

api = falcon.API()

water = Water()

api.add_route('/water', water)