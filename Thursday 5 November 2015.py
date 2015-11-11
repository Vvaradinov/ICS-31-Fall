# ICS 31, Thursday 5 November 2015, 8am

"""
BIG PICTURE:  A programming language lets us model the real world.
    PL gives us:    Things/nouns/objects (ints, floats, lists, namedtuples, ...)
                        Data structures.
                    Actions/verbs/functions, methods, operators, statements,
                        control structures
Data structures:
    Single-valued structures/data: int  float  bool  str
    Multiple-valued data structures:
        lists:  collection of objects of the same category/type
        namedtuples:  package of possibly different-type data fields that
            describe one object
        tuples:  namedtuples without the names:  T[0], T[1], T[2], ...
        files:  give us PERSISTENCE
        [dictionaries, sets, two-dimensional tables, ...:  for later]
    We can combine these to describe more realistic real-world objects

Control statements/structures:
    Single operations:
        + - * /     // (integer division)   % (mod/remainder)
        Functions/methods:    len(L)    L.count('ok')     print()
        Statements:  assert BE      assignment
    We can combine these in a few ways:
        Simple sequence:
            stmt1
            stmt2
            stmt3
            The "stmt"s can be simple statements like print(),
                or they can be structured statements themselves, like if...else.
        Modularity:   Define a function (or a method) to group related actions
            together ("Use the chocolate icing recipe on page 23.")
        Control structure for SELECTION:  if...else,   if...elif...elif...else
        Control structures for REPETITION:  for-loops, while-loops, [recursion]
            for-each loop:
                for CONTROL-VAR in SEQUENCE:
                    BODY

                for x in L:
                    print(x)

            indexing for-loop:
                for i in range(10):
                    BODY

                for i in range(len(L)):
                    L[i] = L[i] + 100
                    print(i, '.', L[i])

                range() function:  range(START, END, STEP)

            For-loops are designed for a set number of iterations (repetitions)
            Sometimes we don't have a specific number; sometimes we just want to
                reapeat until something's true or as long as something's true.
            While-loops are for this situation:
                while BOOLEAN-EXPRESSION:
                    stmt1
                    stmt2
                stmt3  # Not part of the loop body; executed after loop completes.

            Sometimes we want to bail out of a loop early (e.g, we already have
                the answer we need):
                -- Return the first Thai restaurant
                -- Are there any cheap restaurants (price < 10.00, e.g.)?
                -- NOT:  How many Thai restaurants?  List all the cheap restaurants)

            One way:
                found_thai = False
                for r in L:
                    if not found_thai r.cuisine == "Thai":
                        first_thai = r
                        found_thai = True
                return first_thai

            Alternative (assumes there is at least one Thai restaurant):
                for r in L:
                    if r.cuisine == "Thai":
                        first_thai = r
                        break
                return first_thai

            Alternative 2 (doesn't assume at least one Thai restaurant):
                first_thai = ""
                for r in L:
                    if r.cuisine == "Thai":
                        first_thai = r
                        break
                return first_thai

            Alternative 3 (doesn't assume at least one Thai restaurant):
            def find_first_thai_restaurant(L: 'list of Restaurant') -> Restaurant:
                ''' Return first Thai restaurant in L, or empty string if none '''
                first_thai = ""
                for r in L:
                    if r.cuisine == "Thai":
                        first_thai = r
                        return first_thai
                        # or just   return r
                return first_thai
                # or just    return ""  (without the first_thai = "" above)

            Alternative 4 (like 3 but streamlined):
                for r in L:
                    if r.cuisine == "Thai":
                        return r
                return ""   # We got all the way through and found no Thai restaurants

        break:  Out of the current loop
        return: Out of the current FUNCTION
        continue:  Out of the current ITERATION of the loop.

            for i in s:
                statement1
                statement2
                if whatever():
                    continue  # Skip statement3 and 4 THIS TIME THROUGH
                statement3
                statement4
            statement5

            This is equivalent to:

            for i in s:
                statement1
                statement2
                if not whatever():
                    statement3
                    statement4
            statement5

BACK to if-statements
    if a == b:
        return True
    else:
        return False

    This is clumsy and redundant.  Instead, just say
        return a==b


Try this little task:

Write a function called "agelaws" that takes an int representing a person's age
    and returns one of these strings:
        -- "Can neither vote nor drink"
        -- "Can vote but not drink"
        -- "Can both vote and drink"
    in accordance with US law:  Voting at 18 or over, drinking (purchasing
        alcohol) at 21 or over.
"""
VOTINGAGE = 18
DRINKINGAGE = 21

def agelaws(age: int) -> str:
    ''' Return a string categorizing voting and drinking eligibility
    '''
    if age < VOTINGAGE:
        result = "Can neither vote nor drink"
    elif age >= VOTINGAGE and age < DRINKINGAGE:
        result = "Can vote but not drink"
    else:
        result = "Can both vote and drink"
    return result

def agelaws(age: int) -> str:
    ''' Return a string categorizing voting and drinking eligibility
    '''
    if age < VOTINGAGE:
        return "Can neither vote nor drink"
    elif age >= VOTINGAGE and age < DRINKINGAGE:
        return "Can vote but not drink"
    else:
        return "Can both vote and drink"

def agelaws(age: int) -> str:
    ''' Return a string categorizing voting and drinking eligibility
    '''
    if age < VOTINGAGE:
        return "Can neither vote nor drink"
    if age >= VOTINGAGE and age < DRINKINGAGE:
        return "Can vote but not drink"
    else: # Could just as well be   if age >= DRINKINGAGE:
        return "Can both vote and drink"

""" BUGGY:
def agelaws(age: int) -> str:
    ''' Return a string categorizing voting and drinking eligibility
    '''
    if age < VOTINGAGE:
        result = "Can neither vote nor drink"
    if age >= VOTINGAGE and age < DRINKINGAGE:
        result = "Can vote but not drink"
    else: # Could just as well be   if age >= DRINKINGAGE:
        result = "Can both vote and drink"
    return result
"""

def agelaws(age: int) -> str:
    ''' Return a string categorizing voting and drinking eligibility
    '''
    if age < VOTINGAGE:
        result = "Can neither vote nor drink"
    if age >= VOTINGAGE and age < DRINKINGAGE:
        result = "Can vote but not drink"
    if age >= DRINKINGAGE:
        result = "Can both vote and drink"
    return result

def agelaws(age: int) -> str:
    ''' Return a string categorizing voting and drinking eligibility
    '''
    if age < VOTINGAGE:
        result = "Can neither vote nor drink"
    elif age < DRINKINGAGE:
        result = "Can vote but not drink"
    else:
        result = "Can both vote and drink"
    return result

""" BUGGY
def agelaws(age: int) -> str:
    ''' Return a string categorizing voting and drinking eligibility
    '''
    if age < VOTINGAGE:
        result = "Can neither vote nor drink"
    if age < DRINKINGAGE:
        result = "Can vote but not drink"
    else:
        result = "Can both vote and drink"
    return result
"""

assert agelaws(13) == "Can neither vote nor drink"
assert agelaws(17) == "Can neither vote nor drink"
assert agelaws(18) == "Can vote but not drink"
assert agelaws(19) == "Can vote but not drink"
assert agelaws(20) == "Can vote but not drink"
assert agelaws(21) == "Can both vote and drink"
assert agelaws(22) == "Can both vote and drink"
assert agelaws(25) == "Can both vote and drink"
assert agelaws(121) == "Can both vote and drink"
