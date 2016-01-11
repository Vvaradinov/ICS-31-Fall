# ICS 31, Tuesday 24 November 2015, 8am



"""
Programming languages (and their libraries) provide you with a group of
    "Classic Data Structures"

A set (like a mathematical set)
    A collection of items with:
    -- Elements are immutable types
    -- No duplicates
    -- Order doesn't matter
    Useful for:
        * collections of unique items
        * keeping track of memberships (e.g., who's in what major)
    Implemented under the hood with a HASH TABLE (just like dicts),
        meaning instant lookups with "in"
"""
s = {1, 2, 3, 4, 5}
d = {'a':1, 'b':2, 'c':3}
empty_dict = { }
# should be able to say empty_set = { }
empty_set = set()
t = set([2,4,6,8,10])
print(s)
print(d)
print(t)
print(type(empty_dict))
print(type(empty_set))

L = [1,3,2,5,4,2,4,1,3,4,1,5,2,4,2,3,4,2,3,6,5,2,1,2,2,2,2,2,2]
uniqueL = set(L)
print(list(uniqueL))
print('Unique elements in L: ', list(set(L)))



"""
SET OPERATORS

Operators:
    in     not in
Function:
    len()
Operations:
    union( combine values from 2 sets):   x | y
    intersection( everything in common):  x & y
    substraction( set with some items removed): x - y
    symetric difference( in one but not both): x ^ y
"""

print("Union of s and t:", s | t)
print("Intersection s and t:", s & t)
print("Substarction of t from s:",s - t)
print("Symetric difference of t from s:",s ^ t)

"""
Comparison:
    s == t    s != t    s < t (strict subset)   s <= t   s >= t
Methods:
    s.add(i):  Insert i into s (if it's not already there)
    s.remove(i): Remove item, error if it isn't there
    s.discard(i):  Remove item from s, silent if it isn't there
    s.clear():  Remove everything, result is empty set.
    # These are all methods that change s (have side effects)
"""


"""
Write a program to play a dice game "Craps"

Rules:
    Roll two dice (1-6 each):
        Roll 7 or 11, "Natural":  win
        Roll 2, 3, or 12, "Craps":  lose
        Any other number becomes "your point":
            Keep rolling; on each roll:
                -- Roll "point", "make your point": win
                -- Roll 7, "crap out": lose
                -- Roll anything else, roll again
"""

from random import randrange

def roll() -> int:
    ''' Roll 2 dice return value( range 2 to 12 )
    '''
    # This is the wrong distribution:   return randrange(2,13)   # starting number to ending -1 so to have 2 to 12 we need (2,13)
    return randrange(1,7) + randrange(1,7)

'''
for i in range(50):
    print(roll(), roll(), roll(), roll(), roll())
'''

def playOneGame() -> bool:
    ''' Play one game of craps, returning true or false for win or loose with printed narration
    '''
    firstRoll = roll()
    print("Roll is:", firstRoll)
    if firstRoll in {7, 11}:
        print("Natural: Shooter Wins")
        return True
    elif firstRoll in {2, 3, 12}:
        print("Craps: Shooter loses")
        return False
    point = firstRoll
    print("Point is", point)
    while True:
        nextRoll = roll()
        print("Roll is:",nextRoll)
        if nextRoll == 7:
            print("Crapped Out: Shooter Loses")
            return False
        elif nextRoll == point:
            print("Made the point: Shooter Wins")
            return True
'''
playOneGame()
print()
playOneGame()
print()
playOneGame()
print()
playOneGame()
print()



print("Welcome to the Craps game!\n")
while True:
    print("Your game:")
    result = playOneGame()
    print()
    print("Computer's game:")
    result = playOneGame()
    print()
    response = input("Would you like to play again? (y or n):")
    if response == 'n':
        break
'''
print("Welcome to the Craps game!\n")
playerWins = 0
computerWins = 0
for game in range(100):
    print("Your game:")
    result = playOneGame()
    if result:
        playerWins += 1
    print()
    print("Computer's game:")
    result = playOneGame()
    if result:
        computerWins += 1
    print()
    #response = input("Would you like to play again? (y or n):")
    #if response == 'n':
    #   break

print("Player wins", playerWins)
print("Computer wins",computerWins)
print("Thank you for playing.")

print("Distribution of 1000 rolls:")
diceTally = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for rolls in range(1000):
    nextRoll = roll()
    diceTally[nextRoll] += 1

for roll in range(2,13):
    print(roll, '.', diceTally[roll], '#' * (diceTally[roll]//10))
    '''print("{:2d}. {:3d} {}".format(roll, diceTally[roll],
                                   '#' * (diceTally[roll]//10)))'''


