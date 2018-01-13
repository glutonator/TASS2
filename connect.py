import networkx as nx
import matplotlib.pyplot as plt

import airlines_rating as airlines_rat
import airport_rating as airport_rat
import dictionary_air as dict_air
import other
from itertools import islice
import k_shortest_paths as k_sh
import routes_graph as route
import other2

# import networkx as nx
# import matplotlib.pyplot as plt

# import airlines_rating as air_rat
# import routes_graph as route
# import dictionary_air as dict_air

# #opinie linie lotnicze
# dictionary_airlines_rating = dict()
# air_rat.rating_airlines(dictionary_airlines_rating)
# #print(dictionary_airlines_rating)


# #graf pelny
# G=nx.Graph()
# route.add_nodes_to_graph(G)
# route.add_edges_to_graph(G)
# #print(G.node())
# #print(G.edges())

# #slowniki nazwa lotniska/lini lotnicze -nr
# airlines_dict=dict_air.create_airlines_dict()
# airport_dict=dict_air.create_airport_dict()
# #print(airlines_dict)
# ttt=airlines_dict.get('wizz-air')
# print(ttt)
# eeee=dictionary_airlines_rating.get('wizz-air')
# print(eeee.airline_name)
# print(type(eeee))

# #zmiana wag
# tmp = {'overall_rating', 'seat_comfort_rating' , 'cabin_staff_rating','food_beverages_rating','inflight_entertainment_rating','ground_service_rating','wifi_connectivity_rating','value_money_rating','recommended'}
# print(tmp)

# #ustawianie jak bardzo dany parametr ma wplywac na wybor
# param =dict()
# for i in tmp:
#     param[i]=5
# #print(param)

# #pobieranie ratingu
# rating=eeee.dict_airline_param()
# print(rating)

# #route.change_param_all_edges(G,param,rating)
# route.change_param_edge(G,'2965','2990',param,rating)
# #print(G.edges(data=True))
# print("done")


###nowe
tmp = {'overall_rating', 'seat_comfort_rating' , 'cabin_staff_rating','food_beverages_rating','inflight_entertainment_rating','ground_service_rating','wifi_connectivity_rating','value_money_rating','recommended'}

#ustawianie jak bardzo dany parametr ma wplywac na wybor
param =dict()
for i in tmp:
    param[i]=5
airlines_dict=dict_air.create_airlines_dict()
tmp2= {'overall_rating', 'queuing_rating', 'terminal_cleanliness_rating','terminal_seating_rating', 'terminal_signs_rating', 'food_beverages_rating', 'airport_shopping_rating','wifi_connectivity_rating', 'airport_staff_rating', 'recommended'}

#ustawianie jak bardzo dany parametr ma wplywac na wybor
param2 =dict()
for i in tmp2:
    param2[i]=5
airport_dict=dict_air.create_airport_dict()


G=nx.MultiDiGraph()
route.add_nodes_to_graph(G)
route.add_edges_to_graph(G)


dictionary_airlines_rating = dict()
airlines_rat.rating_airlines(dictionary_airlines_rating)
route.add_weight_to_all_edge(G,dictionary_airlines_rating,param,airlines_dict)

dictionary_airports_rating = dict()
airport_rat.rating_airports(dictionary_airports_rating)

dict_name_rat_name_route=other2.rating_airlines_fix()

route.add_weight_to_all_node(G,dictionary_airports_rating,param2,airport_dict,dict_name_rat_name_route)
print(G.edges(data=True))
print("to jest to")
#route.shortes_path_in_graph(G,'3272','3250',4)
route.shortes_path_in_graph(G,'679','350',4)
print("done")