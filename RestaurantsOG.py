# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2015

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    choice = """If you'd like to read restaurants from an existing file,
    type the name of that file; if not, just hit RETURN:  """
    filename = input(choice)
    if filename == "":
        our_rests = Collection_new()
    else:
        our_rests = fill_collection_from_file(filename)
    our_rests = handle_commands(our_rests)
    write_file_from_collection(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
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
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Dish:     " + self.dish + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        input("Please enter the name of the best dish:  "),
        float(input("Please enter the price of that dish:  ")))

def Restaurant_to_tabbed_string(r: Restaurant) -> str:
    ''' Return a string containing the restaurant's fields,
        separated by tabs
    '''
    return r.name + "\t" + r.cuisine + "\t" + r.phone + "\t" + \
            r.dish  + "\t" + str(r.price)
assert Restaurant_to_tabbed_string(Restaurant("Thai Dishes",
                                              "Thai", '333-4444',
                                              'Mee Krob', 8.55)) == \
    "Thai Dishes\tThai\t333-4444\tMee Krob\t8.55"

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

def fill_collection_from_file(filename: str) -> 'list of Restaurant':
    ''' Read restaurant info from file; return collection.
        File has one line for each restaurant, with fields delimited
        by tabs.
    '''
    result = []
    infile = open(filename, 'r')
    for line in infile:
        field_list = line.split("\t")
        new_rest = Restaurant(field_list[0], field_list[1],
                              field_list[2], field_list[3],
                              float(field_list[4]))
        result.append(new_rest)
    infile.close()
    return result

def write_file_from_collection(C: 'list of Restaurant') -> None:
    ''' Write file called restaurants.txt, tab-delimited
    '''
    outfile = open('restaurants.txt', 'w')
    for r in C:
        outfile.write(Restaurant_to_tabbed_string(r) + "\n")
    outfile.close()
    return

restaurants()
