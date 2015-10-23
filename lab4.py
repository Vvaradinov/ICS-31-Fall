# charley2


print('--- part(c)--- ')
print()
print()

def test_number(n: int, s: str) -> bool:
    """Takes number or str and returns True or False"""
    if s == 'even':
        return n % 2 == 0
    else:
        if s == 'odd':
            return n % 2 == 1
        else:
            if s == 'positive':
                return n > 0
            else:
                if s == 'negative':
                    return n < 0
    return
assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')

print(test_number(25, 'even'))
print(test_number(24, 'even'))

print()

def display():
    '''should list each character in any input word
    '''
    name = input()
    for n in name:
        print(n)

display()

print()

def square_list(l: list) -> int:
    '''returns the square of every integer in a list
    '''
    for n in l:
        print(n**2)

square_list([2, 4, 5, 7])

print()

def match_first_letter(x:str, y:list) -> None:
    '''returns every word that starts with a letter 'x' in a list 'y'
    '''
    for f in y:
        if f[0] == x:
            print(f)

match_first_letter('I', ['Iron Man', 'Iron Man 2', 'The Avengers', 'Superman', 'I am Legend'])

print()

def match_area_code(x:list, y:list) -> str:
    '''returns every phone number in a list y that has an area code from list x
    '''
    for f in y:
        for g in x:
            if f[1:4] == g:
                print(f)
    return            

area = ['909', '949']
phone = ['(714)824-1234', '(419)312-8732', '(949)555-1234', '(909)606-9824']
match_area_code(area, phone)

print()

def matching_area_codes(x:list, y:list) -> str:
    '''adds every phone number in a list y that has an area code from list x
    to another list'''
    area_codes_that_match = []
    for f in y:
        for g in x:
            if f[1:4] == g:
                area_codes_that_match.append(f)
    print(area_codes_that_match)
    
matching_area_codes(area, phone)


print()
print(' ---part(d)--- ')
print()
print()

vowel = 'aeiouAEIOU'
def is_vowel(x:str) -> bool:
    '''tells whether the one-character string is a vowel or not
    '''
    return x in vowel

"""
def is_vowel(x:str) -> bool:
    '''tells whether the one-character string is a vowel or not
    '''
    if x in vowel:
        return True
    else:
        return False
    return
"""
print(is_vowel('d'))
print(is_vowel('A'))

print()

def print_nonvowels(x:str) -> None:
    '''prints all nonvowels in a string
    '''
    for b in x:
        if is_vowel(b) == False:
            print(b)
    return

print_nonvowels('iobaqerfaew')
print_nonvowels('ABCDEFGHIJKLMNOPqrstuvwxyz')
        
print()

def nonvowels(x:str) -> str:
    '''prints out all nonvowels, including spaces and punctuation marks
    '''
    result = ''
    for b in x:
        if is_vowel(b) == False:
            result = result + b
    return result
assert nonvowels('bac') == 'bc'
assert nonvowels('bacBOIC') == 'bcBC'
assert nonvowels('work ing?') == 'wrk ng?'
#append doesn't work for strings

print(nonvowels('aouiberawerfa'))
print(nonvowels('.aewf?'))

print()

consonant = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
def consonants(x:str) -> str:
    '''prints all consonants in a string, meaning no spaces or punctuation marks
    '''
    result = ''
    for b in x:
        if b in consonant:
            result = result + b
    return result
assert consonants('abcd') == 'bcd'
assert consonants('?abjJ.UI D') == 'bjJD'

print(consonants('.[]noibguasdofubD'))

print()

def select_letters(x:str, y:str) -> str:
    '''returns vowels in string y if x is v or returns consonants in string y
    if x is c'''
    result = ''
    if x == 'c':
        for b in y:
            if b in consonant:
                result = result + b
    if x == 'v':
        for b in y:
            if b in vowel:
                result = result + b
    return result
assert select_letters('c', 'facetious') == 'fcts'
assert select_letters('v', 'facetious') == 'aeiou'
print(select_letters('c', 'CharlesYoon'), select_letters('v', 'CharlesYoon'))

print()

def hide_vowels(x:str) -> str:
    '''replaces everty vowel in string x with a hyphen '-'
    '''
    result = ''
    for b in x:
        if b in vowel:
            b = '-'
            result = result + b
        else:
            result = result + b
    return result
assert hide_vowels('rat') == 'r-t'
assert hide_vowels('tkinter is strange!') == 'tk-nt-r -s str-ng-!'
print(hide_vowels('ICS31 is fun.'))
    
print()
print(' ---part(e)--- ')
print()
print()

from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
dank_foods = Restaurant('dank foods', 'dank food', 7778888, 'dank dish', 900.0)

def Restaurant_change_price(x: Restaurant, y: float) -> Restaurant:
    '''changes the price of a restaurant x by a number y
    '''
    x = x._replace(price = x.price + y)
    return x

print(Restaurant_change_price(dank_foods, 1.0))
# now it works
print()
print(' ---part(f)--- ')
print()
print()

# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]

#f.1
from operator import attrgetter
def alphabetical(x: RL) -> list:
    """ takes a list of restaurants and returns that list in alphabetical order"""
    sorted(x, key = attrgetter("name"))
    return sorted(x)

print(alphabetical(RL))

print()
print()

#f.2
'''
L_names = []
def alphabetical_names(x: RL) -> L_names:
    """ Takes a list and returns a list of "names" of the restaurants
    """
          
   
print(alphabetical_names(L_names))
'''

#f.3
#L = []
'''def all_Thai(x: list) -> list:
    """ Takes list of Restaurants and returns all Thai Restaurants
    """
    L = list()
    for item in x:
        if item.cuisine == "Thai":
            L = L.append(item)
    return L

        
            
    
            
print(all_Thai(RL))
    
'''
