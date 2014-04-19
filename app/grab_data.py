import requests
from app.apikey import api_key


def get_bus_loc(route, stop, allstops=False):

    url_root = 'http://api.translink.ca/rttiapi/v1/'
    branch = 'buses'

    params = {}

    if not allstops:
        if int(stop) > 0:
            print '----->', stop
            params['stopNo'] = stop
        else:
            params['routeNo'] = route

    url = url_root+branch
    params['apikey'] = api_key

    headers = {'accept': 'application/json'}

    print url, headers, params

    response = requests.get(url, headers=headers, params=params)

    locs = [(e['Latitude'], e['Longitude']) for e in response.json()]

    return locs


if __name__ == "__main__":
    print 'Working....\n-------'
    print get_bus_loc()
    print "-------\ndone!"