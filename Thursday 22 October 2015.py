# ICS 31, Thursday 22 October 2015, 8am

# Mutability and Immutability (and parameters)

# Lists in Python are MUTABLE:  You can change them IN PLACE

L = [10, 20, 30, 40]
print(L)
L[2] = 5000000
print(L)

# Namedtuples (and strings) in Python are IMMUTABLE:  Can't
# change in place; have to make a copy.

from collections import namedtuple
Book = namedtuple('Book', 'title author')
b1 = Book("War and Peace", "Leo Tolstoy")
print(b1)

# It seems reasonable to say:
# b1.author = "Feodor Dostoevesky"
# But we can;t: Attribute error: can't set attribute

s = "Donald Duck"
# s[3] = 'X'
# Likewise, can't do this:  'str' does not support item assignment

"""
Two ways to reflect a new value:
    Use _replace method (namedtuples)
    Make a new object and reassign it to the old variable
"""

"""
Why have this distinction at all?  For efficiency.
    Mutable things are more complicated to build internally
        (to allow for changing in place to something of a different size)
        But "in place" means I don't have to disturb the rest
        (of what might be a very long list)
    Immutable things are simpler to build internally
        But they don't have the flexibility of inserting something
        that's a different size.  You have to make a copy.

EFFICIENCY:
    Machine efficiency (computational resources):
        Processor time
        Memory (RAM) usage
        Secondary storage (disk) usage
        Input and output, network traffic
        Power
    Human efficiency
        for the developer/programmer
        for the end user (HCI, Human-Computer Interaction)

    People time is more expensive than computer time.

"""
L[2:3] = [666,777,888]
print(L)

"""
What happens when we pass items as parameters to a function?
The behavior we see depends on whether the parameter is mutable or immutable.
"""
def add_to_end(s: str, i: str) -> str:
    ''' Return a string with i appended to s
    '''
    s = s + i
    return s
assert add_to_end("Hello", "!!") == "Hello!!"
name = 'Donald Duck'
print(name)
print(add_to_end(name, "!"))
print(name)
## The variable 'name' is unchanged; passing by VALUE (copy)
## No change to the arguent; immutable types are passed as a copy.
## No side effect; no lasting change to the original argument in
##    the calling program.

## What happens if we pass a MUTABLE parameter?

def add_to_end(L: list, i: 'Anything') -> list:
    ''' Return a list with i appended to L
    '''
    L.append(i)   # Gives us a SIDE EFFECT
    return L
assert add_to_end([1,2,3], 4) == [1,2,3,4]
original = [23, 45, 67, 89]
print(original)
print(add_to_end(original, 999))
print(original)
## The variable 'original' is changed by the function:  a SIDE EFFECT.
## This is called passing BY REFERENCE (we pass a link, not a copy)
def add_to_end(L: list, i: 'Anything') -> list:
    ''' Return a list with i appended to L
    '''
    # L.append(i)   # Gives us a SIDE EFFECT
    result = L
    result.append(i) # Gives us a SIDE EFFECT
    return result
    # return L

def add_to_end(L: list, i: 'Anything') -> list:
    ''' Return a list with i appended to L
    '''
    # L.append(i)   # Gives us a SIDE EFFECT
    # result = L
    result = L[:]
    result.append(i) # No side effect:  L[:] makes a copy
    return result
    # return L
def add_to_end(L: list, i: 'Anything') -> list:
    ''' Return a list with i appended to L
    '''
    L.extend(ds)   # Gives us a SIDE EFFECT
    return L
def add_to_end(L: list, i: 'Anything') -> list:
    ''' Return a list with i appended to L
    '''
    L = L + [i]   # Creates a copy; no side effect
    return L
def add_to_end(L: list, i: 'Anything') -> list:
    ''' Return a list with i appended to L
    '''
    L += [i]      # Gives us a side effect.
    return L
assert add_to_end([1,2,3], 4) == [1,2,3,4]
original = [23, 45, 67, 89]
print(original)
print(add_to_end(original, 999))
print(original)

