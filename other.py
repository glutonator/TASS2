#import geopy as gp
from geopy.distance import vincenty

#obliczanie odleglosci na podstawie wpsolrzednych dwoch punktow
def calc_dest(latitude1,longitude1,latitude2,longitude2):
    newport_ri = (latitude1, longitude1)
    cleveland_oh = (latitude2, longitude2)
    out = vincenty(newport_ri,cleveland_oh)
    return out

#rrr= calc_dest(4,4,4,5)
#print(rrr)


class shortes_paths:
    def __init__(self,weigh_list,airports_list,airline_list):
        self.weigh_list=weigh_list
        self.airports_list=airports_list
        self.airline_list=airline_list