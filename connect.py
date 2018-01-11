import networkx as nx
import matplotlib.pyplot as plt

import airlines_rating as air_rat
import routes_graph as route
import dictionary_air as dict_air

#opinie linie lotnicze
dictionary_airlines_rating = dict()
air_rat.rating_airlines(dictionary_airlines_rating)
#print(dictionary_airlines_rating)


#graf pelny
G=nx.Graph()
route.add_nodes_to_graph(G)
route.add_edges_to_graph(G)
#print(G.node())
#print(G.edges())

#slowniki nazwa lotniska/lini lotnicze -nr
airlines_dict=dict_air.create_airlines_dict()
airport_dict=dict_air.create_airport_dict()
#print(airlines_dict)
ttt=airlines_dict.get('wizz-air')
print(ttt)
eeee=dictionary_airlines_rating.get('wizz-air')
print(eeee.airline_name)
print(type(eeee))

#zmiana wag
tmp = {'overall_rating', 'seat_comfort_rating' , 'cabin_staff_rating','food_beverages_rating','inflight_entertainment_rating','ground_service_rating','wifi_connectivity_rating','value_money_rating','recommended'}
print(tmp)

#ustawianie jak bardzo dany parametr ma wplywac na wybor
param =dict()
for i in tmp:
    param[i]=5
#print(param)

#pobieranie ratingu
rating=eeee.dict_airline_param()
print(rating)

#route.change_param_all_edges(G,param,rating)
route.change_param_edge(G,'2965','2990',param,rating)
#print(G.edges(data=True))
print("done")