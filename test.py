
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
    inflight_entertainment_rating,ground_service_rating,wifi_connectivity_rating,value_money_rating ):
        self.airline_name=airline_name
        self.overall_rating = overall_rating
        self.seat_comfort_rating=seat_comfort_rating
        self.cabin_staff_rating=cabin_staff_rating
        self.food_beverages_rating=food_beverages_rating
        self.inflight_entertainment_rating=inflight_entertainment_rating
        self.ground_service_rating=ground_service_rating
        self.wifi_connectivity_rating=wifi_connectivity_rating
        self.value_money_rating=value_money_rating
        self.count=0

    def add(self,overall_rating, seat_comfort_rating , cabin_staff_rating,food_beverages_rating,
    inflight_entertainment_rating,ground_service_rating,wifi_connectivity_rating,value_money_rating ):
        self.overall_rating += overall_rating
        self.seat_comfort_rating+=seat_comfort_rating
        self.cabin_staff_rating+=cabin_staff_rating
        self.food_beverages_rating+=food_beverages_rating
        self.inflight_entertainment_rating+=inflight_entertainment_rating
        self.ground_service_rating+=ground_service_rating
        self.wifi_connectivity_rating+=wifi_connectivity_rating
        self.value_money_rating+=value_money_rating
        self.count+=1

    def __str__(self):
        return "Klass"
    def __repr__(self):
        temp =self.overall_rating.__str__()+self.count.__str__()
        #temp =self.airline_name+self.overall_rating.__str__()+self.count.__str__()
        return (temp)



qqqq = AirLine("hello",0,0,0,0,0,0,0,0)

dictionary_airlines = dict()
dictionary_airlines["qqqq"] = qqqq
#print(dictionary_airlines)
data = []
airline_name_prev="no_name"
airline_name="other_name"
with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\opinie\\test.csv', 'r') as file:
    count =1
    for line in file:
        if count !=1:
            list_info = line.split(',')
            airline_name=list_info[0]            
            if airline_name in dictionary_airlines:
                for i in range(11,18+1):
                    #tu skonczyłem
                    list_of_values 
                dictionary_airlines[airline_name].add(1,1,1,1,1,1,1,1)
                # overall_rating+=list_info[11]
                # seat_comfort_rating+=list_info[12]
                # cabin_staff_rating+=list_info[13]
                # food_beverages_rating+=list_info[14]
                # inflight_entertainment_rating+=list_info[15]
                # ground_service_rating+=list_info[16]
                # wifi_connectivity_rating+=list_info[17]
                # value_money_rating+=list_info[18]

                #usuniecie \n z ostaniego pola
                # temp2=list_info[19]
                # temp = recommended.split('\n')
                # recommended += temp[0]

                #print((recommended))
            else:
                new_airline = AirLine(airline_name,0,0,0,0,0,0,0,0)
                new_airline.add(1,1,1,1,1,1,1,1)
                print(airline_name)
                dictionary_airlines[airline_name]=new_airline
                #out = airline_name_prev +
                data+= [(list_info)]
                #zerowanie danych

            #if (count == 2):
                #print (line)
        count+=1
            #print(type(list_info))
        #print(type(data))

print(dictionary_airlines)
#print(data)