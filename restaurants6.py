# Lopezak1  Vvaradin

__author__ = 'dgk'

# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 d:  Search the collection for restaurant with specific cuisines
 f:  Search the collection for restaurants with a dish by partial name matching
 p:  Print all the restaurants
 e:  Remove (erase) all the restaurants from the collection
 c:  Change prices for the dishes served
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='n':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response == 'e':
            C = Collection_new()
        elif response == 'c':
            n = float(input("Please enter a percentage by which you wish to change the prices: "))
            C = Collection_change_prices(C, n)
        elif response == 'd':
            n = input('Please enter the type of cuisine: ')
            a = Collection_search_by_cuisine(C, n)
            for r in a:
                print(Restaurant_str(r))
        elif response == 'f':
            n = input('Please enter a full or partial dish name: ')
            a = Collection_search_by_partial(C,n)
            for r in a:
                print(Restaurant_str(r))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Average Price:   $" + str(Menu_Price(self.menu)) + "\n" +
        "Average Calories: " + str(Menu_cal(self.menu)) + "\n" +
        "Menu:     " + Menu_str(self.menu) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())

def Restaurant_change_price(r:Restaurant, y:float) -> list:
    '''Raises the price of the entire menu by y'''
    temp = []
    for i in range(len(r.menu)):
        temp.append(Dish_change_price(r.menu[i],y))
    return temp


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_search_by_partial(C:list, name:str) -> list:
    '''Searches for partial matches from the list.
    '''
    result = []
    for r in C:
        for i in r.menu:
            temp = i.name.split()
            for j in temp:
                if j == name:
                    result.append(r)
                    break
    return result

def Collection_search_by_cuisine(C:list, cuisine:str) -> list:
    '''Returns a list of Restaurants whose cuisine matches the input string.
    '''
    result = []
    for r in C:
        if r.cuisine == cuisine:
            result.append(r)
    return result

def Collection_search_by_average_price(C:list, price:float) -> list:
    result = []
    for r in C:
        if Menu_Price(r.menu) <= price:
            result.append(r)
    return result

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]


def Collection_change_prices(C:list, y:float) -> list:
    '''Takes the Collection and a percent change. Returns a list with modified
    prices by the percentage'''
    temp = []
    for r in C:
        temp.append(Restaurant_change_price(r, y))
    return temp

### Dish

Dish = namedtuple('Dish', 'name price calories')

def Dish_change_price(x:Dish, y:float) -> Dish:
    '''Takes Restaurant and number. Returns Restaurant that has price field edited.'''
    if y < 0:
        y = abs(y)
        y = y / 100
        x = x._replace(price = x.price - x.price*y)
    else:
        y = y / 100
        x = x._replace(price = x.price + x.price*y)
    return x

def Dish_str(Dish:Dish) -> str:
    ''' Takes a dish and returns name price and calories'''
    return (Dish.name+ ' ($'+  str(Dish.price)+ ") : "+ str(Dish.calories)+ " cal")
                  
def Dish_get_info() -> Dish:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the price:  ")),
        float(input("Please enter the calories:  ")))     

## Menus

def Menu_str(m:list) -> str:
    '''Takes a menu list and returns the menu in a user friendly form'''
    temp = ""
    for i in m:
        temp += Dish_str(i) + "\n"
    return temp    

def Menu_enter() -> list:
    temp = []
    while True:
        i = input("Would you like to enter a new Dish? Yes or No? ")
        if i == "Yes":
            temp.append(Dish_get_info())
        elif i == "No":
            for r in range(len(temp)):
                print(Dish_str(temp[r]))
            return temp
        else:
            print("Sorry. '", i,"' is an invalid response.") 

def  Menu_Price(m:list) -> float:
    '''Returns avg price of a menu
    '''
    temp = []
    for i in m:
        temp.append(i.price)
    return sum(temp)/len(temp)

def Menu_cal(m:list) -> float:
    '''Returns avg calories of a menu
    '''
    temp = []
    for i in m:
        temp.append(i.calories)
    return sum(temp)/len(temp)
        

restaurants()
