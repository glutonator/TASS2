import networkx as nx
import matplotlib.pyplot as plt

import airlines_rating as airlines_rat
import airport_rating as airport_rat
import dictionary_air as dict_air
import other
from itertools import islice
import k_shortest_paths as k_sh
#import alg_2

def add_nodes_to_graph(G):
    #G.add_node(44,weight=10,latitude=-6.081689834590401,longitude=145.391998291)
    #print(G.nodes(data=True))
    #nody
    #with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\graph\\test2.txt', 'r',encoding="utf8") as file:
    with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\graph\\airports.dat.txt', 'r',encoding="utf8") as file:
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

    #G.add_edge(1,2)
    #print(G.nodes(data=True)) 
    #print(count)      
    # nx.draw(G)
    # plt.show()


#krawedzie
def add_edges_to_graph(G):
    #with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\graph\\test.txt', 'r',encoding="Latin-1") as file:
    with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\graph\\routes.dat.txt', 'r',encoding="Latin-1") as file:
        count =1
        #dictionary_airlines = dict()
        for line in file:
            
            list_info = line.split(',')
            #print(list_info)
            airline_id=list_info[1]
            source_airport_id=list_info[3]
            destination_airport_id=list_info[5]
            if (source_airport_id!='\\N' and destination_airport_id!='\\N'):
                if (G.has_node(source_airport_id)==True and G.has_node(destination_airport_id)==True):
                    #tutaj dodawnie krwaedzi do grafu
                    G.add_edge(source_airport_id,destination_airport_id,weight=1,airline_id=airline_id)
            #trzeba policzyć odleglosc po szerokosci i dl geograficznej miedzy nodami
        #nx.draw(G)
        #plt.show()
        #print(G.edges(data=True))


def change_param_edge(G,source_airport_id,destination_airport_id,map_of_param,map_of_rating):
    for i in map_of_param.items():
        weight_out+=i[1]*(map_of_rating.get(i[0]))
    G[source_airport_id][destination_airport_id]['weight']=weight_out

def change_param_all_edges(G,map_of_param,map_of_rating):
#trzeba jeszce dorzucić jakiś konetenr z opiniami i wtedy zrobic petle nie po wszsytkich krawedziach ale po opiniach liniach lotniczych
    # for u,v,d in G.edges(data=True):
    #     #najpierw licznie wagi do wpisania
    #     rating=4
    #     weight_out=0
    #     for i in map_of_param.items():
    #         #tasiemiec liczacy wartosc wagi
    #         #weight_out+=i[1]*rating
    #         # print(i[0])
    #         # print(i[1])
    #         # print(map_of_rating.get(i[0]))
    #         weight_out+=i[1]*(map_of_rating.get(i[0]))            
    #         #weight_out+=1
    #     #wpisywnaie wagi
    #    print(weight_out)
    #    d['weight']=weight_out
    for i in map_of_rating:
        change_param_edge
        print(type(i))

def set_param(map_of_param,):

    for i in map_of_param.items():
        print(i[1])


#ustawianie zadanaej wagi noda
def add_weight_to_node(G,airport_id,weight):
    for i in G.nodes().data(data=True):
        if i[0]==airport_id:
            i[1]['weight']=weight
            #print(i)
            #print(i[1]['weight'])

#ustawiwanie wag do wszystkich nodow w opparciu o opinie
def add_weight_to_all_node(G,dict_airports_rating,dict_airport_param,dict_name_airport_id):
    count =0
    count2=0
    for i in dict_airports_rating.items():
        weight_out=0
        #print(i)
        #liczenie wagi dla konkretnego lotniska        
        for j in i[1].dict_airport_param().items():
            wght=dict_airport_param[j[0]]
            rat=j[1]
            weight_out+=rat*wght
            #print(j)
            #print(wght,rat,weight_out)
        #print(weight_out)
        weight_out=1/weight_out
        airport_id=dict_name_airport_id.get(i[0])
        #airport_id=dict_name_airport_id.get('warsaw-chopin-airport')
        #print(i[0])
        
        if airport_id is not None:
            count+=1
            #print(i[0])
        count2+=1
    #print(count,count2)

#znajowanie wszystkich krwaedzi danej lini lotniczej i ustawianie wagi + poprawka na odleglosc
def add_weight_to_edge(G,airline_id,weight):
    #print((G))    
    #print(G.edge_iter())
    #for i in G.edges().data(data=True):
    for i in G.edges(data=True):
        #print(i)
        #wizz-air to 5461
        #print(i)
        if i[2]['airline_id']==airline_id:
            #print(i[0],i[1])
            #print(i[0],i[1],G.node[i[0]],G.node[i[1]])
            lat1=G.node[i[0]]['latitude']
            lon1=G.node[i[0]]['longitude']
            lat2=G.node[i[1]]['latitude']
            lon2=G.node[i[1]]['longitude'] 
            #wyciaganie z nodow wag by miala wplyw na krawedzie i suzkiwanie polaczen
            wght1=G.node[i[0]]['weight']
            wght2=G.node[i[1]]['weight']
            wght_node=wght1*wght2
            print(wght_node)
            #######
            dist=other.calc_dest(lat1,lon1,lat2,lon2)
            #print(dist)
            i[2]['weight']=weight*dist.km*wght_node
            #print(i[2]['weight'])
            #print(i)
        #print("aaaaaaaaaaaaaaaaaaaaaaa ",i)
    #print("sdadas")


#ustawianie wag do wszystkich krawedzi w oparciu o opinie
def add_weight_to_all_edge(G,dict_airlines_rating,dict_airline_param,dict_name_airline_id):
    print(G.node['5']['latitude'])
    print(G.node['5'])
    for i in dict_airlines_rating.items():
        weight_out=0
        wght=1
        
        
        #liczenie wagi dla konkretnej lini lotniczej
        for j in i[1].dict_airline_param().items():
            #print(dict_airline_param[j[0]])
            wght=dict_airline_param[j[0]]
            rat=j[1]
            #weight_out+=j[1]*wght
            weight_out+=rat*wght
            #print(i,j[0],j[1])
        weight_out=1/weight_out
        #print("wwww",weight_out)
        airlines_id=dict_name_airline_id.get(i[0])
        #jesli opinia dotyczy lini ktora jest w pliku route.dat.txt
        if airlines_id is not None:
            #tutaj trzeba jeszcze dorobic zaleznosc weight_out od km
            add_weight_to_edge(G,airlines_id,weight_out)

        #print(i,dict_name_airline_id.get(i[0]))
        #add_weight_to_edge(G, ,weight_out )
        #print(i[1].dict_airline_param())

#wyznaczanie najkrotszej sciezki
def shortes_path_in_graph(G,source_airport_id,destination_airport_id,k):
    
    # out=k_sh.k_shortest_paths(G,source_airport_id,destination_airport_id,k=2,weight='weight')
    # print("sdads",out)


    #print(nx.dijkstra_path(G,source_airport_id,destination_airport_id))
    #print(nx.all_pairs_dijkstra_path(G))
    #qqqq=nx.single_source_dijkstra(G,source_airport_id,destination_airport_id,5)
    #k=3

    #list_of_routes=nx.shortest_simple_paths(G, source_airport_id, destination_airport_id, weight='weight')
    
    #kopiowanie grafu
    H=G.copy()
    airports_list=list()
    weigh_list=list()
    airline_list=list()
    for qq in range(0,k+1): 
        #aaaaaa=nx.dijkstra_path(G, source_airport_id, destination_airport_id, weight='weight')
        tmp=nx.single_source_dijkstra(H, source_airport_id, destination_airport_id, weight='weight')
        weigh_list.append(tmp[0])
        airports_list.append(tmp[1])
        airline_list_tmp=list()  
        #aaaaaa=nx.single_source_dijkstra(G, destination_airport_id,source_airport_id, weight='weight')
        print(tmp)
        count=0
        ptr=tmp[1]
        for i in tmp[1]:
            if count==0:
                ptr=i
                count+=1
            else:
                wght=99999999
                
                #znaleznie krawedzi o najmniejszej wadze ktora zaostalu uzyta
                for (u, v,kk,c) in H.edges(data=True,keys=True):
                    ### c-slonik dannych kk-klucz edgow               
                    if(u==ptr and v==i):
                        #print(G.edge[ptr,i]['weight'])
                        print("j",u, v, c)
                        if(wght>c['weight']):
                            wght=c['weight']
                            kkey=kk                           
                            air_id=c['airline_id']
                            print("wid",air_id)
                print("id",air_id)
                airline_list_tmp.append(air_id)
                #przechodzę po calej trasie i zbieram nr_lini_lotniczych


                print("przed_usu",i,ptr,kkey,wght)
                H.remove_edge(ptr,i,kkey)
                        
                #tmp=nx.single_source_dijkstra(H, source_airport_id, destination_airport_id, weight='weight')
                print(ptr,i,tmp)              
                ptr=i
        
        #airports_list.append(tmp[1])                
        airline_list.append(airline_list_tmp)
    #weigh_list.append(tmp[0])
        #aassa
    print("outout")
    print(weigh_list)
    print(airports_list)
    print(airline_list)
    return other.shortes_paths(weigh_list,airports_list,airline_list)
    #G.remove_edge('679','1569')
    #G.remove_edge('679','1569')
    #G.remove_edge('679','351')
#    G.remove_edge('679','351')
    
    # aaaaaa=nx.single_source_dijkstra(G, source_airport_id, destination_airport_id, weight='weight')
    # print(aaaaaa)
    
    #aaaaaa=nx.single_source_dijkstra(G, source_airport_id, destination_airport_id)
    #print(aaaaaa)
    #aaaaaa=nx.all_pairs_dijkstra_path(G)
    #rrrrr=aaaaaa.__next__()
    #yyyyy=aaaaaa.__iter__()
    # for i in aaaaaa:
    #     if i[0]=='1':
    #         print("aaaaaaaaaaaaaa",i[0],i[1])
    #print("hell",rrrrr[0])
    #rrrrr=aaaaaa.__next__()
    #print("hell",rrrrr[0])
    #print("done")
    # list_of_routes=list(islice(nx.shortest_simple_paths(G, source_airport_id, destination_airport_id, weight='weight'), k))
    # for i in list_of_routes:
    #     count=0
    #     #prv=i[0]
    #     for j in i:
    #         if count==0:
    #            prv=j
    #            count+=1
    #         else:
    #             print("dsadsa",prv,j,G[prv][j]['airline_id'])
    #             prv=j
               
    #         print(j)
    #     print(i)




    # list_of_out = list(islice(nx.shortest_simple_paths(G, source_airport_id, destination_airport_id, weight='weight'), k))
    # for path in list_of_out:
    #     print(path)

        
    #wwwww=nx.all_pairs_dijkstra_path(G)
    #wwwww[source_airport_id]  
    # wwwww.__next__()
 
    #print(wwwww)   
    # print(wwwww.__next__())
    #print("done")   
    #print(wwwww.__next__())
    #wwwww(1,2)
    #print("done")
    

# # # ###nowe
# # # tmp = {'overall_rating', 'seat_comfort_rating' , 'cabin_staff_rating','food_beverages_rating','inflight_entertainment_rating','ground_service_rating','wifi_connectivity_rating','value_money_rating','recommended'}
# # # #print(tmp)
# # # #ustawianie jak bardzo dany parametr ma wplywac na wybor
# # # param =dict()
# # # for i in tmp:
# # #     param[i]=5
# # # airlines_dict=dict_air.create_airlines_dict()
# # # tmp2= {'overall_rating', 'queuing_rating', 'terminal_cleanliness_rating','terminal_seating_rating', 'terminal_signs_rating', 'food_beverages_rating', 'airport_shopping_rating','wifi_connectivity_rating', 'airport_staff_rating', 'recommended'}

# # # #print(tmp)
# # # #ustawianie jak bardzo dany parametr ma wplywac na wybor
# # # param2 =dict()
# # # for i in tmp2:
# # #     param2[i]=5

# # # airport_dict=dict_air.create_airport_dict()

# # # #G=nx.Graph()
# # # G=nx.MultiDiGraph()
# # # add_nodes_to_graph(G)
# # # add_edges_to_graph(G)
# # # #for i in G.edges(data=True):
# # #     # if (i[0]==1 and i[1]==2):
# # #     #     print("sadoisdjasod")
# # #     #print(i[0],i[1])
# # #     #print(i[2]['airline_id'])

# # # dictionary_airlines_rating = dict()
# # # airlines_rat.rating_airlines(dictionary_airlines_rating)
# # # add_weight_to_all_edge(G,dictionary_airlines_rating,param,airlines_dict)

# # # dictionary_airports_rating = dict()
# # # airport_rat.rating_airports(dictionary_airports_rating)
# # # #add_weight_to_node(G,'12049',33)
# # # add_weight_to_all_node(G,dictionary_airports_rating,param2,airport_dict)
# # # print(G.has_node('1'))
# # # print(G.node['1'])
# # # print("to jest to")
# # # #shortes_path_in_graph(G,'3272','3250')
# # # shortes_path_in_graph(G,'679','350',4)
# # # #for path in shortes_path_in_graph(G,'679','340',4):
# # # #    print(type(path))
# # # #shortes_path_in_graph(G,'679','350')
# # # #shortes_path_in_graph(G,'679','340')

# # # #print(G.nodes(data=True))

# # # #print(G.edges(data=True))

# # # #print(airlines_dict)
# # # #######


# # # #G=nx.Graph()
# # # # add_nodes_to_graph(G)
# # # #add_edges_to_graph(G)
# # # #test_test(G,'5461','20')
# # # # #change_param_edge(G,'2965','2990',400)
# # # # print(G.edges(data=True))

# # # # #change_param_all_edges(G)
# # # # print("\n")
# # # # print(G.edges(data=True))

# # # # tmp = {'overall_rating', 'seat_comfort_rating' , 'cabin_staff_rating','food_beverages_rating','inflight_entertainment_rating','ground_service_rating','wifi_connectivity_rating','value_money_rating','recommended'}
# # # # print(tmp)

# # # # param =dict()
# # # # for i in tmp:
# # # #     param[i]=5
# # # # #print(param)
# # # # print("nowy")
# # # # set_param(param)
# # # # #param[]