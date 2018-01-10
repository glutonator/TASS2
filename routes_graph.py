import networkx as nx
import matplotlib.pyplot as plt



def add_nodes_to_graph(G):
    #G.add_node(44,weight=10,latitude=-6.081689834590401,longitude=145.391998291)
    #print(G.nodes(data=True))
    #nody
    with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\graph\\test2.txt', 'r',encoding="utf8") as file:
    #with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\graph\\airports.dat.txt', 'r',encoding="utf8") as file:
        count =1
        #dictionary_airlines = dict()
        for line in file:
            
            list_info = line.split(',')
            #print(list_info)
            airport_id=list_info[0]
            airport_name=list_info[1]
            latitude=list_info[6]
            longitude=list_info[7]
            #tutaj dodawnie nodow do grafu
            G.add_node(airport_id,weight=1,latitude=latitude,longitude=longitude)
            count+=1

    G.add_edge(1,2)
    print(G.nodes(data=True)) 
    print(count)      
    # nx.draw(G)
    # plt.show()


#krawedzie
def add_edges_to_graph(G):
    with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\graph\\test.txt', 'r',encoding="Latin-1") as file:
        count =1
        #dictionary_airlines = dict()
        for line in file:
            
            list_info = line.split(',')
            print(list_info)
            airline_id=list_info[1]
            source_airport_id=list_info[3]
            destination_airport_id=list_info[5]
            #tutaj dodawnie krwaedzi do grafu
            G.add_edge(source_airport_id,destination_airport_id,weight=1,airline_id=airline_id)
            #trzeba policzyć odleglosc po szerokosci i dl geograficznej miedzy nodami
        #nx.draw(G)
        #plt.show()
        print(G.edges(data=True))


def change_param_edge(G,source_airport_id,destination_airport_id,weight):
    G[source_airport_id][destination_airport_id]['weight']=weight

def change_param_all_edges(G,map_of_param):
#trzeba jeszce dorzucić jakiś konetenr z opiniami i wtedy zrobic petle nie po wszsytkich krawedziach ale po opiniach liniach lotniczych
    for u,v,d in G.edges(data=True):
        #najpierw licznie wagi do wpisania
        rating=4
        for i in map_of_param.items():
            #tasiemiec liczacy wartosc wagi
            weight_out+=i*rating
        #wpisywnaie wagi
        d['weight']=weight_out

def set_param(map_of_param,):

    for i in map_of_param.items():
        print(i[1])


# G=nx.Graph()
# add_edges_to_graph(G) 
# change_param_edge(G,'2965','2990',400)
# print(G.edges(data=True))
# change_param_all_edges(G)
# print("\n")
# print(G.edges(data=True))

tmp = {'overall_rating', 'seat_comfort_rating' , 'cabin_staff_rating','food_beverages_rating','inflight_entertainment_rating','ground_service_rating','wifi_connectivity_rating','value_money_rating','recommended'}
print(tmp)

param =dict()
for i in tmp:
    param[i]=5
#print(param)
print("nowy")
set_param(param)
#param[]