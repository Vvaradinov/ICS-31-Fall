# ICS 31, Tuesday 13 October 2015, 8am

"""
Things/objects/nouns
Actions/functions,methods,operations/verbs
    Combine actions:
    Sequence
    Function calling (Use the chocolate icing recipe on page 23)
    Selection:  Choosing one alternative action or another,
        based on the result of a boolean expression (if statements)
    Repetition:  Repeat a block of code:
        -- For each item in a sequence (for-each loop, for i in L:)
        -- For a series of numbers (for-loop, for n in range(10):)
        -- As long as some condition is true (while-loop)
        -- Recursion (ICS 32)
"""
'''
D = ["Huey", 'Dewey', 'Louie']
print(D)
duck_count = 0
for item in D:
    print(item, "is a cool duck.")
    duck_count = duck_count + 1
print("There were", duck_count, "ducks.")
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
R1 = Restaurant('Taillevent', 'French', '01-22-33-44-55-66',
                'Escargots', 45.00)
R2 = Restaurant('Thai Dishes', 'Thai', '333-4444', "Larb Gai", 9.50)
R3 = Restaurant("McDonald's", 'Burgers', '333-4332', 'Big Mac', 3.50)
RL = [R1, R2, R3]
print(RL)
for r in RL:
    print(r.name, "is a ", r.cuisine, "restaurant serving",
          r.dish, "for $", r.price, " (phone ", r.phone, ")")
"""
for-each loop syntax:
    for VARIABLE in SEQUENCE:
        STATEMENT(S)    # This is the BODY of the loop
    The variable is called the CONTROL VARIABLE, but it's just a variable.

for-each loop semantics:
    Assign the first item in the sequence to the control variable.
    Do the body of the loop (with the control variable having that value)
    End of list?  Done.
    Otherwise, assign the second item in the sequence to the control variable.
    Do the body of the loop again (with the c.v. having that second value)
    End of list?  Done.
    Otherwise ...
"""
for i in range(5):
    print("Hello" * i)
"""
Semantics are similar; c.v. gets first item in range, then next, then next,
until the end
"""
print("Here are the ducks:")
for duck_num in range(len(D)):
    print(duck_num+1, ".  ", D[duck_num])
print("That's it.")

"""
while-loop:  When you want to repeat an indefinite number of times.
    Syntax:
        while BOOLEAN-EXPRESSION:
            STATEMENT(S)    # Body of the loop
    Semantics:
        Evaluate the B.E. (True or False).  If false, skip body entirely.
            If true, do the body.  Then go back (Evaluate, ...)

Special pattern with while loops:  "N-and-a-half-times loop"
    while True:  # Essentially "do forever" ... but wait
        ... FIRST PART OF BODY
        if BOOLEAN-EXPRESSION:
            break       # Ejector seat:  Quit loop now, from middle
        ... REST OF THE BODY
    NEXT STATEMENT

Example ("PSEUDOCODE" -- leave out some details, kind of a sketch):
while True:
    Print menu
    Read user's command
    If command is valid:
        break   #We're cool; go on to process this command
    print("Sorry; that's not a valid command. Try again"
Process the command
"""
'''
### Restaurants Program Version 1.
### Organize in "Model/View" style:  The model is how the
### program "thinks" internally about restaurants and lists;
### The view is the user interface (here a basic text-based console,
### but some day maybe a tablet or a watch).

def restaurants() -> None:
    ''' Main Restaurants program:  Create and maintain a
        database of restaurants
    '''
    print("Welcome to the Restaurants Program")
    print()
    our_rests = []   # Here we could read a collection in from a file
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

def handle_commands(RC: 'list of Restaurant') -> 'list of Restaurant':
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






restaurants()   # Start the whole thing up
