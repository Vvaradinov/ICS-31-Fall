#ICS 31, Thursday 15 October 2015, 8 AM

"""
Continuing the restaurants program from where we left off
"""

### Restaurants Program Version 1.
### Organize in "Model/View" style:  The model is how the
### program "thinks" internally about restaurants and lists;
### The view is the user interface (here a basic text-based console,
### but some day maybe a tablet or a watch).

## VIEW PART:  What the user sees.  This would change for
## different platforms, like tablet or smartphone or a
## desktop app outside of the Python shell.

def restaurants() -> None:
    ''' Main Restaurants program:  Create and maintain a
        database of restaurants
    '''
    print("Welcome to the Restaurants Program")
    print()
    our_rests = Collection_new()
    # Here we could read a collection in from a file
    our_rests = handle_commands(our_rests)
    # Here we could write our collection out to a file.
    print()
    print("Thank you.  Good-bye.")
    return

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 q:  Quit
 """
'''
def handle_commands(RC: 'list of Restaurant') -> 'list of Restaurant':
    pass   # We call this skeleton/shell of a function a PROGRAM STUB
'''
def handle_commands0(RC: 'list of Restaurant') -> 'list of Restaurant':
    ''' Print menu, accept and execute commands to maintain list.
    '''
    while True:
        command = input(MENU)
        if command == 'q':
            return RC     # Jump out of this while loop; we're done
        else:
            print("You typed: ", command)

def handle_commands1(RC: 'list of Restaurant') -> 'list of Restaurant':
    ''' Print menu, accept and execute commands to maintain list.
    '''
    while True:
        command = input(MENU)
        if command == 'q':
            return RC     # Jump out of this while loop; we're done
        else:
            if command == 'a':
                print("You want to add a restaurant")
            else:
                if command == 'r':
                    print("You want to remove a restaurant")
                else:
                    if command == 'p':
                        print("You want to print the collection")
                    else:
                        if command == 's':
                            print("You want to search the collection")
                        else:
                            print("You typed: ", command)

## This is syntactically a little cumbersome.
## There's a shorthand using "elif".
## This coding pattern is called an "if-ladder"


def handle_commands(RC: 'list of Restaurant') -> 'list of Restaurant':
    ''' Print menu, accept and execute commands to maintain list.
    '''
    while True:
        command = input(MENU)
        if command == 'q':
            return RC     # Jump out of this while loop; we're done
        elif command == 'a':
            # print("You want to add a restaurant")
            RC = Collection_add(RC, Restaurant_get_info())
        elif command == 'r':
            # print("You want to remove a restaurant")
            restaurant_to_remove = input("Please enter the name of the restaurant " +
                                         "to remove:  ")
            RC = Collection_remove_by_name(RC, restaurant_to_remove)
        elif command == 's':
            # print("You want to search for a restaurant")
            restaurant_to_find = input("Please enter the name of the restaurant " +
                                         "to find:  ")
            matching_rests = Collection_search_by_name(RC, restaurant_to_find)
            print(Collection_to_str(matching_rests))
        elif command == 'p':
            # print("You want to display the restaurants")
            print(Collection_to_str(RC))
    return RC

## MODEL PART:  The program's internal way of thinking about
## its data

## RESTAURANT
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
R1 = Restaurant('Taillevent', 'French', '01-22-33-44-55-66',
                'Escargots', 24.50)
R2 = Restaurant('Thai Dishes', 'Thai', '334-4433', 'Mee Krob', 9.50)
R3 = Restaurant('Thai Touch', 'Thai', '444-3333', 'Larb Gai', 12.00)
#print(R1)
#print([R1,R2,R3])

def Restaurant_print(R: Restaurant) -> None:
    ''' Print a Restaurant object readably.
    '''
    print('Name:     ', R.name, "\n",
          'Cuisine:  ', R.cuisine, "\n",
          'Phone:    ', R.phone, "\n",
          'Dish:     ', R.dish, "\n",
          'Price:    $', R.price, "\n\n",sep='')
    return

## It would be more flexible to write a function that
## RETURNS a printable restaurant string

def Restaurant_to_str(R: Restaurant) -> str:
    ''' Return a human-readable string representing restaurant data
    '''
    return 'Name:     ' + R.name + "\n" + \
          'Cuisine:  ' + R.cuisine + "\n" + \
          'Phone:    ' + R.phone + "\n" + \
          'Dish:     ' + R.dish + "\n" + \
          'Price:    $' + str(R.price) + "\n\n"
TestString = """Name:     Taillevent
Cuisine:  French
Phone:    01-22-33-44-55-66
Dish:     Escargots
Price:    $24.5

"""
assert Restaurant_to_str(R1) == TestString
#print("'",TestString[-1],"'",sep="")
#print("'",Restaurant_to_str(R1)[-1],"'",sep="")
#print("'",TestString,"'",sep="")
#print("'",Restaurant_to_str(R1),"'",sep="")

def Restaurant_get_info() -> Restaurant:
    ''' Prompt user for fields of a restaurant; create and return
    '''
    n = input("Please enter the restaurant's name:  ")
    c = input("Please enter the kind of food served:  ")
    ph = input("Please enter the phone number:  ")
    d = input("Please enter the name of the best dish:  ")
    p = input("Please enter the price of that dish:  ")
    return Restaurant(n, c, ph, d, float(p))

# R4 = Restaurant_get_info()
# print(Restaurant_to_str(R4))

#print(Restaurant_to_str(R1))
#print(Restaurant_to_str(R2))


## COLLECTION
## Implemented (built) as a simple Python list of Restaurant objects
## (But that's a decision that might change some day.)

def Collection_new() -> 'list of Restaurant':
    ''' Return a new (empty) collection [an empty list]
    '''
    return [ ]
assert Collection_new() == [ ]

def Collection_add(C: 'list of Restaurant', R: Restaurant) -> 'list of Restaurant':
    ''' Return list of Restaurants with parameter R added at end
    '''
    return C + [R]
assert Collection_add(Collection_new(), R1) == [R1]
assert Collection_add([R3, R2], R1) == [R3, R2, R1]

def Collection_to_str(C: 'list of Restaurant') -> str:
    ''' Return a  string representing the whole collection
    '''
    result = ""
    for r in C:
        result = result + Restaurant_to_str(r)
    return result
assert Collection_to_str(Collection_new()) == ""
assert Collection_to_str([R1, R2, R3]) == \
    Restaurant_to_str(R1) + Restaurant_to_str(R2) + Restaurant_to_str(R3)
        
def Collection_search_by_name(C: 'list of Restaurants',
                              looking_for: str) -> 'list of Restaurant':
    ''' Return a collection containing thos restaurants in C that
        match the second parameter
    '''
    result = [ ]
    for r in C:
        if r.name == looking_for:
            result.append(r)   # result = result + [r]  an alternative
    return result
assert Collection_search_by_name([R1,R2,R3], 'Thai Dishes')== [R2]
assert Collection_search_by_name([R1,R2,R3], "McDonald's") == [ ]
assert Collection_search_by_name([ ], "Taillevent") == [ ]
assert Collection_search_by_name([R2,R1,R2,R3], "Thai Dishes") == [R2, R2]
# The last test shows us collecting multiple restaurants with the same name

def Collection_remove_by_name (C: 'list of Restaurant',
                               to_remove: str) -> 'list of Restaurant':
    ''' Remove named restaurant from collection (return remaining collection)
    '''
    result = [ ]
    for r in C:
        if r.name != to_remove:
            result.append(r)  # To remove, keep the ones that DON'T match
    return result
# Remove single item from list
assert Collection_remove_by_name([R1,R2,R3], 'Thai Dishes')== [R1, R3]
# Remove item not on the list in the first place (no change)
assert Collection_remove_by_name([R1,R2,R3], "McDonald's") == [R1, R2, R3]
# Remove from an empty list (still empty)
assert Collection_remove_by_name([ ], "Taillevent") == [ ]
# Remove multiple items with same name from list
assert Collection_remove_by_name([R2,R1,R2,R3], "Thai Dishes") == [R1, R3]
# Remove item from single-item list (result empty)
assert Collection_remove_by_name([R1], "Taillevent") == [ ]


restaurants()   # Start the whole thing up
