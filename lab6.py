#Lopezak1    Vvaradin 

print() #blank
print("<----------------C.1--------------->")
print() #blank

def contains(x:str , y:str) -> bool:
    ''' Function takes input as two strings and returns true if the second string is in the
    first string '''
    if x.count(y) >= 1:
        return True
    else:
        return False
assert contains('banana', 'ana') == True
assert not contains('racecar', 'ck') == True

print(contains("string", "ig"))

print() #blank
print("<----------------C.2--------------->")
print() #blank

def sentence_stats(x:str) -> None:
    '''Takes a sentece 'x' as a parameter and returns information about the sentence'''
    a = []
    b = []
    char = len(x)
    b = x.split()
    words = len(b)
    for i in range(len(b)):
        a.append(len(b[i]))
    print('Characters: ', char)
    print('Words: ', words)
    print('Average word length: ', (sum(a)/len(a)))
    return

sentence_stats("I love UCI")

print() #blank
print("<----------------C.3--------------->")
print() #blank

def initials(x:str) -> str:
    '''Takes input representing a full name and returns capitalized initials'''
    a = ""
    b = x.split()
    for i in b:
        a += i[0].upper()
    return a
assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'

print(initials('Adam Kristopher Lopez'))

print() #blank
print("<----------------d.1--------------->")
print() #blank

from random import randrange

for i in range(0,50):
    print(randrange(11))

print()

for i in range(0,50):
    print(randrange(7))

print() #blank
print("<----------------d.2--------------->")
print() #blank

def roll2dice() -> None:
    '''Takes no argument and returns a number that reflects the random roll of two dice'''
    for i in range(51):
        a = randrange(1,7)
        b = randrange(1,7)
        print(a + b)
    return

roll2dice()

print() #blank
print("<----------------d.3--------------->")
print() #blank

def distribution_of_rolls(x:float) -> None:
    '''Takes the number of times to roll the die and prints the distribution of rolls'''
    c = []
    z = []
    y = []
    for i in range(x):
        a = randrange(1,7)
        b = randrange(1,7)
        c.append(float(a + b))
    for j in range(11):
        x = 2 + j
        y.append(c.count(x))
        w = c.count(x)
        z.append(round((w/len(c))*100,1))
    for k in range(11):
        t = 2 + k
        k = '{}: {} ( {} % ) {} '.format(t, y[t-2], z[t-2], '*' * y[t-2])
        print(k)
    return

distribution_of_rolls(200)

print() #blank
print("<----------------E--------------->")
print() #blank

alphabet = 'abcdefghijklmopqrstuvwxyz'

def Rotate(key: int) -> str:
    """ Shifting the alphabet by the key we want to cipher """
    rotate = ""
    for letter in alphabet:
        if letter in alphabet:
            rotate += alphabet[(alphabet.index(letter) + key) % (len(alphabet))]
    return rotate


def Caesar_encrypt(s: str, key: int) -> str:
    """ Return cipher text"""
    table = str.maketrans(alphabet,
                          Rotate(key))
    return s.translate(table)
print(Caesar_encrypt("encrypt this shit", 4))


def Caesar_decrypt(s: str, key: int) -> str:
    """ Returns plain text"""
    table = str.maketrans(Rotate(key),
                          alphabet)
    return s.translate(table)
print(Caesar_decrypt("ingvctx xlmw wlmx", 4))


print() #blank
print("<----------------f.1--------------->")
print() #blank

t = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        ","" ]

def print_line_numbers(x:list) -> None:
    '''Takes a list of strings and prints each string preceded by a line number
    '''
    for i in range(len(x)):
        s = ' {:5}: {:5}'.format(i+1,x[i])
        print(s)
    return

print_line_numbers(t)

print() #blank
print("<----------------f.2--------------->")
print() #blank

def stats(x:list) -> None:
    '''Takes a list of strings and prints statistics about the list
    '''
    empty = []
    nonempty = []
    char = []
    charNonEmpty = []
    for i in range(len(x)):
        char.append(len(x[i]))
        if x[i] == "":
            empty.append(x[i])
        else:
            nonempty.append(x[i])
            charNonEmpty.append(len(x[i]))
    totalAvg = round(sum(char)/len(char),2)
    nonEmptyAvg = round(sum(charNonEmpty)/len(charNonEmpty),2)
    print(' {:5} {:5}'.format(len(char),'lines in the list'))
    print(' {:5} {:5}'.format(len(empty),'empty lines'))
    print(' {:5} {:5}'.format(totalAvg,'average  characters per line'))
    print(' {:5} {:5}'.format(nonEmptyAvg,'average characters per non-empty line'))
    return

stats(t)

def list_of_words(x:list) -> list:
    '''takes a list of strings and returns a list of individual words with
    all white space and punctuation removed (except for apostrophes/single quotes)
    '''
    L_1 = []
    L_2 = []
    for i in x:
        L_1.append(i.split())
    for i in L_1:
        L_2.append(i)
    return L_2

print(list_of_words(t))



        
        
    
            

            










