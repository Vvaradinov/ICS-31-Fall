# ICS 31, Thursday 29 October 2015, 8am

## STRING METHODS (continued)

s = "Donald Duck"
print(s.upper()) #lower case
print(s.lower()) # upper case
t = "Four score and seven years ago ... "
print(t.title())

print("How many s characters in Mississippi?",  'Mississippi'.count('s'))

print("Mississippi".replace('s', '***')) # replace method for strings
m = "Mississippi"
print(m.replace("s", "***")) 
print(m)

x = """         Is this

where       the Mississippi
    is today?

"""

print(x.split()) # takes away all the white space
wordlist = x.split()
print(" ".join(wordlist)) # joins the strings with some white space
print(",  ".join(wordlist)) # joins the strings with comas in between
print("\n".join(wordlist)) # joins the string on a new line

print("--->" + x + "<---")
print("--->" + x.strip() + "<---") #strip takes out white space in begginig and end
print("--->" + x.lstrip() + "<---") #strip takes out white space on left
print("--->" + x.rstrip() + "<---") #strip takes out white space on right


w = "Four***score*and*seven****years ago...."
print(w.split("*")) #splits for every * in the string


## TRANSLATION

def our_lower(s:str) -> str:
    """ Return all-lower-case version of s"""
    ## Two setps
    ## 1. Make a "TRANSLATION TABLE"
    table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                          'abcdefghijklmnopqrstuvwxyz') #sets up the translation
    ## 2.Use the table to do the translation
    return s.translate(table) #makes the actuall translation    
assert our_lower("MissISSippI") == "mississippi"
print(our_lower("For SCORE and SeVen Years ago..."))


#Another application: Remove punctuation
no_punct_table = str.maketrans('.,:;?""',     # transaltion has to match
                               '       ')     # with equal lenght
y = 'Four, score and "seven" years ago: our fathers....?'
print(y.translate(no_punct_table)) # y is the str and no_punct_table is the table
print(y.translate(no_punct_table).split())

n1 = "Programmer, Paula"
n2 = "Anteater, Arnold"

# Turn these into first-name-frist form

def first_and_last(last_comma_first: str) -> " list of str":
    """ Return a two item list, [ First name, last name]
    """
    comma_position = last_comma_first.find(",") #find the comma
    lastname = last_comma_first[:comma_position] # goes to the comma
    firstname = last_comma_first[comma_position+1:] # goes from the comma to the end
    return [firstname.strip(), lastname] #strip gets the space out of there

assert first_and_last(n1) == ["Paula", "Programmer"]
assert first_and_last(n2) == ["Arnold", "Anteater"]


## STRING FORMATTING
## How do we get dollars-and-cents amounts to look like 25.00$
## How can we control spacing/alignment of the things we print

## This will use the modern Python forma, with the format() method
## The book uses this, too.
## There's another, old-fashnioned form that we won't use.


from collections import namedtuple
Dish = namedtuple('Dish', ' name price calories')
d1 = Dish("Paht Woon Sen", 12.50, 335)

#Say we want to display Dishesh to look this way
# Paht Woon Sen ($12.50): 335 cal

# FORMATSTRING.format(LISTOFEXPRESSIONS TO FORMAT)
#THIS RETURNS A STRING, WHICH WE CAN PRINT OR DO WHATEVER
print()
print("---{}---".format(d1.name)) 
# curly braces are placeholders for our string we put in the string there
s = ("Name: {} ${}".format(d1.name, d1.price)) #each one in order will replace with the curly places
print(s)

print("{} (${}): {} cal.".format(d1.name, d1.price, d1.calories))


## To format each item further, we add things inside the {}
## {   :   }
## Left side of the colon: Change order of arguments
## just leave it empty
## Right side of colon: the FIELD WIDTH
## how many spaces/columns on the page screen to devote to this


print("{} (${:6.2f}): {} cal.".format(d1.name, d1.price, d1.calories))
# 6.2 == we are going to reserve 6 spaces in the output of which 2 are after the decimal point
# f == floating point number
print("{} (${:8.2f}): {} cal.".format(d1.name, d1.price, d1.calories))
print("{} (${:10.2f}): {} cal.".format(d1.name, d1.price, d1.calories))
print()
print("{} (${:6.0f}): {} cal.".format(d1.name, d1.price, d1.calories))
print("{} (${:6.1f}): {} cal.".format(d1.name, d1.price, d1.calories))
print("{} (${:6.2f}): {} cal.".format(d1.name, d1.price, d1.calories))
print("{} (${:6.3f}): {} cal.".format(d1.name, d1.price, d1.calories))
print()


("{} (${:0.2f}): {} cal.".format(d1.name, d1.price, d1.calories))
# 0.2 == 0 = takes as much spaces as we need automatically 2= 2 spaces afterdecimal point
print()
print()

def dish_to_str(d: Dish) -> str:
    ''' Return a dish represented as dishname ($price): calories cal.
    '''
    return "{} (${:0.2f}): {} cal.".format(d.name, d.price, d.calories)
assert dish_to_str(d1) == "Paht Woon Sen ($12.50): 335 cal."

d2 = Dish("Larb Gai", 11.50, 350)
d3 = Dish("Golden Wing", 105.00, 1250)
print(dish_to_str(d1))
print(dish_to_str(d2))
print(dish_to_str(d3))
print()
print()
def dish_to_str_aligned(d: Dish) -> str:
    ''' Return a dish represented as dishname ($price): calories cal.
        with the fields having fixed widths '''
    return "{:15s} (${:8.2f}): {:4d} cal.".format(d.name, d.price, d.calories)
# assert dish_to_str(d1) == "Paht Woon Sen ($12.50): 335 cal."
# s == string f == float d == demical number (int)
d2 = Dish("Larb Gai", 11.50, 350)
d3 = Dish("Golden Wing", 105.00, 1250)
print(dish_to_str_aligned(d1))
print(dish_to_str_aligned(d2))
print(dish_to_str_aligned(d3))

