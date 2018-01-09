
class AirLine:
    airline_name="pppppp"
    # overall_rating=5
    # seat_comfort_rating=0
    # cabin_staff_rating=0
    # food_beverages_rating=0
    # inflight_entertainment_rating=0
    # ground_service_rating=0
    # wifi_connectivity_rating=0
    # value_money_rating=0
    # count=0

    def __init__(self,airline_name,overall_rating, seat_comfort_rating , cabin_staff_rating,food_beverages_rating,
    inflight_entertainment_rating,ground_service_rating,wifi_connectivity_rating,value_money_rating,recommended ):
        self.airline_name=airline_name
        self.overall_rating = overall_rating
        self.seat_comfort_rating=seat_comfort_rating
        self.cabin_staff_rating=cabin_staff_rating
        self.food_beverages_rating=food_beverages_rating
        self.inflight_entertainment_rating=inflight_entertainment_rating
        self.ground_service_rating=ground_service_rating
        self.wifi_connectivity_rating=wifi_connectivity_rating
        self.value_money_rating=value_money_rating
        self.recommended=recommended
        self.count=0

    def add(self,overall_rating, seat_comfort_rating , cabin_staff_rating,food_beverages_rating,
    inflight_entertainment_rating,ground_service_rating,wifi_connectivity_rating,value_money_rating, recommended):
        self.overall_rating += overall_rating
        self.seat_comfort_rating+=seat_comfort_rating
        self.cabin_staff_rating+=cabin_staff_rating
        self.food_beverages_rating+=food_beverages_rating
        self.inflight_entertainment_rating+=inflight_entertainment_rating
        self.ground_service_rating+=ground_service_rating
        self.wifi_connectivity_rating+=wifi_connectivity_rating
        self.value_money_rating+=value_money_rating
        self.recommended+=recommended
        self.count+=1

    def add_list(self,list_of_param):
        self.overall_rating+=list_of_param[0]
        self.seat_comfort_rating+=list_of_param[1]
        self.cabin_staff_rating+=list_of_param[2]
        self.food_beverages_rating+=list_of_param[3]
        self.inflight_entertainment_rating+=list_of_param[4]
        self.ground_service_rating+=list_of_param[5]
        self.wifi_connectivity_rating+=list_of_param[6]
        self.value_money_rating+=list_of_param[7]
        self.recommended+=list_of_param[8]
        self.count+=1
        #     self.overall_rating += overall_rating
        #     self.seat_comfort_rating+=seat_comfort_rating
        #     self.cabin_staff_rating+=cabin_staff_rating
        #     self.food_beverages_rating+=food_beverages_rating
        #     self.inflight_entertainment_rating+=inflight_entertainment_rating
        #     self.ground_service_rating+=ground_service_rating
        #     self.wifi_connectivity_rating+=wifi_connectivity_rating
        #     self.value_money_rating+=value_money_rating
        #     self.recommended+=recommended
        #     self.count+=1

    def __str__(self):
        return "Klass"
    def __repr__(self):
        temp =self.recommended.__str__()+" "+self.count.__str__()
        #temp =self.overall_rating.__str__()+" "+self.count.__str__()
        #temp =self.count.__str__()
        #temp =self.airline_name+self.overall_rating.__str__()+self.count.__str__()
        return (temp)

    def avrage(self):
        self.overall_rating = self.overall_rating/self.count
        self.seat_comfort_rating=self.seat_comfort_rating/self.count
        self.cabin_staff_rating=self.cabin_staff_rating/self.count
        self.food_beverages_rating=self.food_beverages_rating/self.count
        self.inflight_entertainment_rating=self.inflight_entertainment_rating/self.count
        self.ground_service_rating=self.ground_service_rating/self.count
        self.wifi_connectivity_rating=self.wifi_connectivity_rating/self.count
        self.value_money_rating=self.value_money_rating/self.count
        self.recommended=self.recommended/self.count


def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

#konwersja str na int, jesli nie jest to wartosc domyslna
def rating_fix(value,default_value=77.0):
    if not isfloat(value):
        return default_value
    else:       
        return float(value)

#usuniecie "" z danych
def delete_string(word):
    if(word[len(word)-1]=="\n"):
        word = word[0:len(word)-1]
    out = word[1:len(word)-1]
    return out

 

#sddsds=delete_string("\"dsds\"\n")
#sddsds=delete_string("\"dsds\"")
#print(sddsds)
#qqqq = AirLine("hello",0,0,0,0,0,0,0,0,0)

dictionary_airlines = dict()
#dictionary_airlines["qqqq"] = qqqq
#print(dictionary_airlines)


#airline_name="other_name"

#with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\opinie\\test.csv', 'r',encoding="utf8") as file:
with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\opinie\\airline.csv', 'r',encoding="utf8") as file:
    count =1
    #tttt=0
    for line in file:
        if count !=1:
            list_info = line.split('","')
            #sprawdzenie czy sie dobrze wszytko wczytalo jesli nie, to pomija linijke
            if (len(list_info)==20):
                airline_name=(list_info[0])[1:len(list_info[0])]

                tmp =list()
                for i in range (11,19):
                    tmp.append(rating_fix(list_info[i]))
                
                recom_temp=(list_info[19])[0:len(list_info[19])-2]
                #print(list_info[11])
                tmp.append(rating_fix(recom_temp))

                #print(tmp)
                
                # if airline_name=='air-canada-rouge':
                #     for i in range (0,20):
                #         print(i, list_info[i])
                #     tttt+=1
                #     print(("licznik",tttt))  

                if airline_name in dictionary_airlines:
                    dictionary_airlines[airline_name].add_list(tmp)
                    #dictionary_airlines[airline_name].add(list_info[11],list_info[12],list_info[13],list_info[14],list_info[15],list_info[16],list_info[17],list_info[18],recommended)
                    #usuniecie \n z ostaniego pola
                    # temp2=list_info[19]
                    # temp = temp2.split('\n')
                    # recommended = temp[0]
                    #dictionary_airlines[airline_name].add(list_info[11],list_info[12],list_info[13],list_info[14],list_info[15],list_info[16],list_info[17],list_info[18],recommended)
                else:
                    new_airline = AirLine(airline_name,0,0,0,0,0,0,0,0,0)
                    new_airline.add_list(tmp)
                    print(airline_name)
                    dictionary_airlines[airline_name]=new_airline

        count+=1

#wyznaczanie sredniej
print("odsaksado")
for i in dictionary_airlines.items():
    i[1].avrage()

print(dictionary_airlines)
