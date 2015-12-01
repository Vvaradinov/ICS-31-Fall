# ICS 31, Tuesday 1 December 2015, 8am


#namedtuple in a set


"""
Avoiding duplicate code.
    Programming languages give us a variety of ways of capturing commonalities.
    Functions, parameters, more....


    

"""

def matches_cuisine(R: Restaurant, C:str) -> bool:
    """ Return True if R's cuisine matches C """
    return R.cuisine == C


def all_serving_cuisine(RL: "list of restaurants", C: str) -> "list of Restaurants":
    """ Return a list of those Restaurants in RL that serve cuisine C """
    result = [ ]
    for R in RL:
        if matches_cuisine(R, C):
            result.append(R)
    return result
assert all_serving_cuisine(RL, 'Thai') == [R4,R5,R6,R23]
assert all_serving_cuisine(RL, 'Peruvian') == [ ]
assert all_serving_cuisine(RL, 'Pizza') == [R12]


def is_cheap(R:Restaurant) -> bool:
    """ Return True if R's price is $10 or below"""
    return R.price <= 10
assert not is_cheap(R26)
assert is_cheap(R5)


def all_cheap(RL: "List of Restaurant") -> "list of Restaurant":
    """ Return a list of those Restaurants in RL that are cheap ($10 or under) """
    result = []
    for R in RL:
        if is_cheap(R):
            result.append(R)
    return result



def all_matches(RL: "list of Restaurant", test: "func Restaurant -> bool") -> " list of restaurant":
    """ Return a list of those Restaurants in RL that pass the test """
    result = []
    for R in RL:
        if test(R):
            result.append(R)
    return result
assert all_matches(RL, is_Thai) == [R4, R5, R6, R23]

"""
A function that returns a bool is called a PREDICATE
    is_cheap is a 'predicate on restaurants". So is is_Thai.
Rearranging code to campture commonalities is called REFACTORING.


One pending issue: Do we have to define each predicate with def pred(..)?
    For now, yes.
Can we capture this pattern in a higher-level way?
    Here, we've been aifting through a list, keeping some and discarding others.

Here's another pattern: Suppose we want the NAMES of all the Thai restaurants.
    So far, we've been gathering a list of Restaurant objects( all 5 fields)


"""

def extract_names(RL: "list of Restaurants") -> "list of str":
    """ Return a list of the names of each restaurant in RL"""
    result = []
    for R in RL:
        result.append(R.name)
    return result
assert extract_names(all_matches(RL, is_French)) == ["Taillevent",
                                                     "La Tour D'Argent",
                                                     "Pascal" ]



def extract_names_and_phones(RL: "List of Restaurants") -> "list of str":
    """ Return a list of the names and phones of each restaurant in RL """
    result = []
    for R in RL:
        result.append((R.name, R.phone))
    return result


"""

A FILTERING operation selects some items from a collection ( e.g., the Thai
    restaurants or the cheap ones)
A MAPPING operation transforms each item in a collection (e.g., Restaurant
    to a string with name, or to (name,phone) tuple)

We can write functions to capture these patterns.
"""

def filter (f: "func X -> bool", L: "list of X") -> "list of X":
    """ Return those items on L that pass the predicate f """
    result = [ ]
    for i in L:
        if f(i):
            result.append(i)
    return result
assert filter(is_Thai, RL) == [R4 , R5, R6, R23]


def map (f: "func X -> Y", L: "List of X") -> "list of Y":
    """ Return each item ion L with f applied to it """
    result = []
    for i in L:
        result.append(f(i))
    return result

def rest_name(R:Restaurant) -> str:
    """ Return Restaurants's name field """
    return R.name

def rest_name_phone(R: Restaurant) -> "(str, str)":
    """ Return (name,phone) tuple for the restaurant R """
    return (R.name, R.phone)
"""
The concept of treating functions as data/objects (e.g., as parameters
to some other function as aobve) is called HIGHER-ORDER FUNCTIONS.


WE can combine these to do more powerful things pretty easily.

Say we want the phone numbers of all the Thai and French Restaurants.
"""

Thai_or_French = filter(is_Thai, RL) + filter(is_French, RL)
TF_phones = map(rest_phone, Thai_or_French)

"""
Shorthand for creating functions on the fly ( instead of def f(....) -> ....)
Using a "lambda expression"
A lambda expression's value is a function.
"""

def double (n: int) -> float:
    return n * 2

double = lambda n: n*2
is_Ethiopian = lambda R: R.cuisine == "Ethiopian"
filter(lambda R: R.cuisine == "Ethiopian", RL)
