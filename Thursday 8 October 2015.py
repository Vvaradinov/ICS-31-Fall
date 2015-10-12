# ICS 31, Thursday 8 October 2015, 8am

#FUNCTION DEFINITION

"""
Syntax
    def NAME (PARAMETER-LIST) -> RETURN-TYPE:
       ''' DOCSTRING COMMENT / PURPOSE STATEMENT '''
       BODY-OF-FUNCTION( zero or more statements)
       return EXPRESSION (what goes "out the spout" to the calling program)
       assert BOOLEAN-EXPRESSION    (examples of correct behaviour/test)
       ...

Semantics of function calling:
    NAME(ARGUMENTS)

"""

def double(n: int) -> int:
    """ Return 2 times the parameter """
    return 2*n
assert double(3) == 6
assert double(0) == 0
assert double(-15) == -30
print(double(17))
print(double(double(10)))
x = double(3) + double(5 + 9)
print(x)


#Most of the time, we write functions to return a value
#(rather than to print).

#But some functions don't. They have SIDE EFFECTS.

def print_ten_stars()  -> None:
    """ Print ten stars in a row """
    print('**********')
    return
print_ten_stars()


def print_n_stars(n: int) -> None:
    """Prints the specified number of stars  """
    print('*' * n)
    return
print_n_stars(1)
print_n_stars(0)
print_n_stars(12)


def print_n_copies(n: int, s: str) -> None:
    """ Prints n copies of the specified string"""
    print(s * n)
    return
print_n_copies(3, '*')
print_n_copies(10, 'OK')
    
"""
    " Computer Science is the art of turning constants into variables "
    -- Doanld E. Knuth (Stanford), America's most famous CS
"""

# We can turn this into a (more flexible) function that RETURNS its value

def n_copies(n: int, s: str) -> str:
    """Return a string with n copies of the parameter string"""
    return s * n
assert n_copies(5, 'x') == 'xxxxx'
assert n_copies(0, 'hello') == ''
assert n_copies(2, "Okay") == 'OkayOkay'
a = n_copies(3, '*')
b = n_copies(10 , 'OK')
# We have more flexibility with what we can do with n_copies's result
print(a,b)


"""
Things/objects/nouns/data
Actions/.../verbs/procedures
    Statements (assert,return,assignment, ...)
    Operations + - / *
    Functions
    Methods   (L.sort())

We can combine actions using:
    Sequence
       print("hello")
       print("Good-bye")
       salary = hours *  rate
    Nesting
       x = (y + z) * 10
       print("You are", int(input("How old are you?")), 'years old')
       print("Next year you will be", 1 + int(input("How old are you?"),
       'years old')
    Function definitions
    Selection: Choose one action or another depending on some boolean expression
                              if-statement
    Repetition: Repeat some statements, Various ways:
      -- Repeat for each item in sequence [for-loop]
      -- Repeat a specified number of times [for-loop]
      -- Repeat as long as something (some BOOLEAN expression) is true
                    [while-loop]
"""

print()
temperature = 85
# ...
print("Here's what to wear today")
if temperature < 60:
    print("Put on a sweater")
print("Have a good day")
print()
# Another example
print("Here's what to wear today")
if temperature < 60:
    print('Put on a sweater')
else:
    print('Put on a T-shirt')
print("Have a good day")

"""
Syntax of an if-statement
    if BOOLEAN-EXPRESSION:
      STATEMENT(S)              #the body of the if-statement

    if BOOLEAN-EXPERSSION
       STATEMENT(S)             #the body of the if-statement
    else:
       STATEMENT(s)             #the body of the else-statement/else part

Semantics of version 1:
    Evaluate the B.E. (True or False)
    If it's true, execute the body of the if-statement
    If it's false, don't do anything special
    [Then in either case, continue with the following statement

Semantics of version 2:
    Evaluate the B.E. (True or False)
    If it's true, execute the body of the if-statement
    If it's false, execute the body of the else-part
    [Then in either case, continue with the following statement]

REPETITION
    For-loops:  One way that goes through a sequence ("for-each")
                One way that counts
"""
print()
L = ['Huey', 'Dewey', 'Louie']
for item in L:
    print(item)
    print('is a cool duck.')

"""
Syntax:
    for VARIABLE in SEQUENCE:
        STATEMENT(S)         # Body of loop

Semantics:
    Set VARIABLE to value of first item in SEQUENCE
    Do the body of the loop with that value for VARIABLE
    Set VARIABLE to the value of the second item in SEQUENCE
    Do the body of the loop with that value for VARIABLE
    Continue for each item in the sequence.
""" 

