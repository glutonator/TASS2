import airlines_rating as air_rat
import routes_graph as route

#opinie linie lotnicze
dictionary_airlines_rating = dict()
air_rat.rating_airlines(dictionary_airlines_rating)
print(dictionary_airlines_rating)

#dodać słonik i dodać route i wszystkie trzy dane polączyć