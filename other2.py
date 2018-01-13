#dictionary_airlines
def rating_airlines_fix():
    out = dict()
    #with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\rating\\test.csv', 'r',encoding="utf8") as file:
    with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\airport_fix.txt', 'r',encoding="utf8") as file:
        count =1
        #tttt=0
        for line in file:
            list_info = line.split(',')
            name_rating=list_info[2]
            name_route=list_info[3]
            #print(tmp2)
            name_route=name_route[0:len(list_info[3])-1]
            #print(name_rating,name_route)
            name_route=name_route.replace(" ", "-")
            name_route=name_route.lower()
            #print(name_rating,name_route)
            out[name_rating]=name_route
    return out
            
rating_airlines_fix()