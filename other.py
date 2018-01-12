#import geopy as gp
from geopy.distance import vincenty

#obliczanie odleglosci na podstawie wpsolrzednych dwoch punktow
def calc_dest(latitude1,longitude1,latitude2,longitude2):
    newport_ri = (latitude1, longitude1)
    cleveland_oh = (latitude2, longitude2)
    out = vincenty(newport_ri,cleveland_oh)
    return out

rrr= calc_dest(4,4,4,5)
print(rrr)
