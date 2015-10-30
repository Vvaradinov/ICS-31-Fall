# vvaradin

#c
def Dish(x: str, y: float, z: float) -> None:
    """ Takes 3 arguments, name, price, calories"""
    pass
    
#c.1

from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')
d1 = Dish("Spaghetti Carbonara", 12.50, 350.0)
d2 = Dish("Joe's Stake", 25.00, 200.0)
d3 = Dish("Moe's BBQ", 50.00, 500.0)


#c.2
print("--- c.2 ---")
def Dish_str(d_obj: d1) -> str:
    """ Takes a dish object and returns a string"""
    print(d_obj.name, '$',d_obj.price, ":", d_obj.calories)
    return

print(Dish_str(d1))
print()
print()


#c.3
print("--- c.3 ---")
def Dish_same(d1_obj: d1, d2_obj: d2) -> bool:
    """ Takes 2 dish objects and returns True if the names and their calories are equal"""
    if d1_obj.name ==  d2_obj.name and d1_obj.calories == d2_obj.calories:
        return True
    else:
        return False

print(Dish_same(d1,d2))
print()
print()

#c.4
print("--- c.4 ---")
def Dish_change_price(d_obj: Dish, num: float) -> Dish:
    """ Takes in Dish and number and returns"""
    d_obj = d_obj._replace(price = d_obj.price + (num * 0.01 * d_obj.price))
    return d_obj

print(Dish_change_price(d1, 100))
#c.5
print("--- c.5 ---")
def Dish_is_cheap(d_obj: Dish, num: float) -> bool:
    """ Takes in a Dish and a number and returns True if the dish's price is less than the number"""
    if d_obj.price < num:
        return True
    else:
        return False

print(Dish_is_cheap(d1, 20))
print()
print()

#c.6
print("--- c.6 ---")
d4 = Dish("Cury", 2.00, 15.00)
d5 = Dish("Meat Balls", 4.00, 50.00)
d6 = Dish("Beef", 5.00, 25.00)
d7 = Dish("Salmon", 50.00, 50.00)
d8 = Dish("Chicken", 70.00, 40.00)
d9 = Dish("Cereal", 25.00, 110.0)
DL = [d1,d2,d3,d4,d5]
DL2 = [d6,d7,d8,d9]
DL.extend(DL2)

def Dishlist_display(l: DL) -> str:
    """ Takes list of dishes and returns a string each on new line"""
    print(d1.name, d1.price, d1.calories, ('\n'),
          d2.name, d2.price, d2.calories, ('\n'),
          d3.name, d3.price, d3.calories, ('\n'),
          d4.name, d4.price, d4.calories, ('\n'),
          d5.name, d5.price, d5.calories, ('\n'),
          d6.name, d6.price, d6.calories, ('\n'),
          d7.name, d7.price, d7.calories, ('\n'),
          d8.name, d8.price, d8.calories, ('\n'),
          d9.name, d9.price, d9.calories, ('\n'))
    return('')

print(Dishlist_display(DL))
print()
print()

#c.7
print("--- c.7 ---")
def Dishlist_all_cheap(l: list, num: float) -> bool:
    """ Takes in a list and returns a bool"""
    for l_obj in l:
        if not Dish_is_cheap(l_obj,num):
            return False
    return True
        


# TA: Answered
print(Dishlist_all_cheap(DL, 10.00))
    


#c.8
print("--- c.8 ---")
def Dishlist_change_price(l: list, num: float) -> list:
    """ Takes a list and a number (percentage) and returns a list of dishesh with the new price"""
    l_new = []
    for l_obj in l:
        l_new.append(l_obj._replace(price = l_obj.price - num * l_obj.price))
    return l_new #returns the whole body of the function instead for only the first value in the list

print(Dishlist_change_price(DL, 0.75))
print()
print()

#c.9
print("--- c.9 ---")
def Dishlist_prices(l: list) -> float:
    """ Takes a list and returns a list of numbers containing just the prices"""
    l_prices = []
    for l_obj in l:
        l_prices.append(l_obj.price)
    return l_prices #returns the whole body of the function instead for only the first value in the l
print(Dishlist_prices(DL))
print()
print() 

#c.10
print("--- c.10 ---")
def Dishlist_average(l: list) -> float:
    """ Takes a list of dishesh and return the average price of the dishesh"""
    x = sum(Dishlist_prices(l))
    y = len(Dishlist_prices(l))
    return x / y
# This work 
print(Dishlist_average(DL))
print()
print()

#c.11
print("--- c.11 ---")
def Dishlist_keep_cheap(l: list, num: float) -> list:
    """ Takes a list of dishesh and a numb and returns a list of the original dishesh that are less than a given numb"""
    l_original = []
    for l_obj in l:
        if l_obj.price < num:
            l_original.append(l_obj) 
    return l_original
print(Dishlist_keep_cheap(DL, 10.00))   
print()
print()

#c.12
print("--- c.12 ---")
ND1 = Dish("Denish Noodles",  24.50, 250.00)
ND2 = Dish("English Noodles",  48.50, 120.00)
ND3 = Dish("Irish Noodles", 32.00, 350.00)
ND4 = Dish("Chinnese Noodles", 10.95, 120.00)
ND5 = Dish("Thai Noodles", 8.50, 140.00)
ND6 = Dish("Korean Noodles",  9.00, 220.00)
ND7 = Dish("Japannese Noodles",  3.95, 120.00)
ND8 = Dish("Russian Noodles", 3.75, 450.00)
ND9 = Dish("French Noodles", 7.50, 100.00)
ND10 = Dish("Italian Noodles", 2.50, 25.00)
ND11 = Dish("German Noodles",  4.50, 240.00)
ND12 = Dish("Slovenian Noodles", 12.95, 120.00)
ND13 = Dish("Serbian Noodles", 12.50, 450.00)
ND14 = Dish("Bulgarian Noodles", 13.50, 250.00)
ND15 = Dish("Armenian Noodles",  24.50, 120.00)
ND16 = Dish("Romanian Noodles", 25.00, 390.00)
ND17 = Dish("Greek Noodles", 24.50, 235.00)
ND18 = Dish("Turkish Noodles", 21.50, 55.55)
ND19 = Dish("American Noodles", 8.50, 220.00)
ND20 = Dish("Norwegian Noodles", 11.50, 210.00)
ND21 = Dish("Swiss Noodles", 5.50, 120.00)
ND22 = Dish("Swedish Noodles", 25.50, 430.00)
ND23 = Dish("Taiwanese Noodles", 15.50, 300.00)
ND24 = Dish("Hooland Noodles", 5.50, 250.00)
ND25 = Dish("Ukranian Noodles", 35.50, 149.00)

ND = [ND1,ND2,ND3,ND4,ND5,ND6,ND7,ND8,ND9,ND10,ND11,ND12,ND13,ND14,ND15,ND16,ND17,ND18,ND19,ND20,ND21,ND22,ND23,ND24,ND25]

def before_and_after():
    ND = [ND1,ND2,ND3,ND4,ND5,ND6,ND7,ND8,ND9,ND10,ND11,ND12,ND13,ND14,ND15,ND16,ND17,ND18,ND19,ND20,ND21,ND22,ND23,ND24,ND25]
    s = int(input(("What % change do you want: ")))
    list_n = []
    print(ND)
    print()
    for l_obj in ND:
        list_n.append(l_obj._replace(price = l_obj.price + s *0.01* l_obj.price))
    return list_n



print(before_and_after())
print()
print()



print("--- e.1 ---")

Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])

r3 = Restaurant('Pascal', 'French', '940-752-0107', [Dish('Escargots', 12.95, 250),
                                                     Dish('Poached Salmon', 18.50, 550),
                                                     Dish('Rack of Lamb', 24.00, 850)])
print(r3)

print()
print()
print("--- e.2 ---")

def Restaurant_first_dish_name(R: Restaurant) -> Restaurant:
    """ Takes a restaurant and returns the name of the first dish in the menu"""
    for obj in R.menu:
        return obj.name
print(Restaurant_first_dish_name(r1))

print()
print()
print("--- e.3 ---")

def Restaurant_is_cheap(R: Restaurant, num: float) -> bool:
    """ Takes a R and a number and returns bool"""
    for obj in R.menu:
        if Dishlist_average(R.menu) <= num:
            return True
        else:
            return False
            

print(Restaurant_is_cheap(r1, 11.75))
print()
print()
print("--- e.4 ---")
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])


'''def Collection_raise_prices(R: Restaurant) -> Restaurant:
    """ Takes the collection and raises the prize of every dish by 2.50"""
    for obj in R.menu:
        obj._replace(price = obj.price + 2.50)
        return obj
print(Collection_raise_prices(r1))

'''
