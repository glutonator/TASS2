class Airport:

    def __init__(self,airport_name,overall_rating, queuing_rating, terminal_cleanliness_rating,
    terminal_seating_rating, terminal_signs_rating, food_beverages_rating, airport_shopping_rating,
    wifi_connectivity_rating, airport_staff_rating, recommended):
        self.overall_rating=overall_rating
        self.airport_name=airport_name
        self.queuing_rating=queuing_rating
        self.terminal_cleanliness_rating=terminal_cleanliness_rating
        self.terminal_seating_rating=terminal_seating_rating
        self.terminal_signs_rating=terminal_signs_rating
        self.food_beverages_rating=food_beverages_rating
        self.airport_shopping_rating=airport_shopping_rating
        self.wifi_connectivity_rating=wifi_connectivity_rating
        self.airport_staff_rating=airport_staff_rating
        self.recommended=recommended
        self.count=0

    def add(self,airport_name,overall_rating, queuing_rating, terminal_cleanliness_rating,
    terminal_seating_rating, terminal_signs_rating, food_beverages_rating, airport_shopping_rating,
    wifi_connectivity_rating, airport_staff_rating, recommended):
        self.overall_rating+=overall_rating
        self.queuing_rating+=queuing_rating
        self.terminal_cleanliness_rating+=terminal_cleanliness_rating
        self.terminal_seating_rating+=terminal_seating_rating
        self.terminal_signs_rating+=terminal_signs_rating
        self.food_beverages_rating+=food_beverages_rating
        self.airport_shopping_rating+=airport_shopping_rating
        self.wifi_connectivity_rating+=wifi_connectivity_rating
        self.airport_staff_rating+=airport_staff_rating
        self.recommended+=recommended
        self.count+=1
    
    def add_list(self,list_of_param):
        self.overall_rating+=list_of_param[0]
        self.queuing_rating+=list_of_param[1]
        self.terminal_cleanliness_rating+=list_of_param[2]
        self.terminal_seating_rating+=list_of_param[3]
        self.terminal_signs_rating+=list_of_param[4]
        self.food_beverages_rating+=list_of_param[5]
        self.airport_shopping_rating+=list_of_param[6]
        self.wifi_connectivity_rating+=list_of_param[7]
        self.airport_staff_rating+=list_of_param[8]
        self.recommended+=list_of_param[9]
        self.count+=1

    def __repr__(self):
        temp =self.recommended.__str__()+" "+self.count.__str__()
        return (temp)

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

#with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\opinie\\test2.csv', 'r',encoding="utf8") as file:
with open('C:\\Users\Filip\\Documents\GitHub\\TASS2\\dane\\opinie\\airport.csv', 'r',encoding="utf8") as file:
    count =1
    dictionary_airlines = dict()
    for line in file:
        if count !=1:
            list_info = line.split('","')
            if (len(list_info)==20):
                airport_name=(list_info[0])[1:len(list_info[0])]

                tmp =list()
                for i in range (10,19):
                    tmp.append(rating_fix(list_info[i]))
                
                recom_temp=(list_info[19])[0:len(list_info[19])-2]
                tmp.append(rating_fix(recom_temp))

                if airport_name in dictionary_airlines:
                    dictionary_airlines[airport_name].add_list(tmp)
                else:
                    new_airport = Airport(airport_name,0,0,0,0,0,0,0,0,0,0)
                    new_airport.add_list(tmp)
                    print(airport_name)
                    dictionary_airlines[airport_name]=new_airport

        count+=1


print(dictionary_airlines)