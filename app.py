import falcon
from water import Water

api = application = falcon.API()

water = Water()

api.add_route('/water', water)