import json
import falcon

class Water(object):
    def on_get(self,req,resp):
        waterAPI = {
                    'data':[
                                {
                                    'time':"5am - 8am",
                                    'quantity':1000
                                },
                                {
                                    'time':"9am - 11pm",
                                    'quantity':1000
                                },
                                {
                                    'time':"11pm - 2pm",
                                    'quantity':1500
                                },
                                {
                                    'time':"5am - 8am",
                                    'quantity':800
                                },
                                {
                                    'time':"5am - 8am",
                                    'quantity':100
                                },
                            ]
                    }
        resp.body = json.dumps(waterAPI)
        resp.status = falcon.HTTP_200

