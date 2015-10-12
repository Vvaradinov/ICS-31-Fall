# ICS 31, Tuesday 6 October 2015, 11am

temps = [78, 79, 78, 95, 92, 92, 99, 88]
ducks = ['Huey', 'Dewey', 'Louie', 'Daisy', 'Scrooge', 'Donald']
one_duck = "Donald"

print(temps[0:3])
print(ducks[0:3])
print(one_duck[0:3])
"""
"""
from collections import namedtuple
Student = namedtuple('Student', 'name ID GPA major')
s1 = Student("Programmer, Peter", 33334444, 3.25, "CSE")
s2 = Student("Anteater, Andrea", 11112222, 3.95, "CS")
one_GPA = 3.99
s4 = Student("Programmer, Paula", 33333333, one_GPA, "BIM")
print(s4)
one_GPA = 2.5
print(s4)
s3 = Student("Anteater, Peter", 22223333, 3.05, "PoliSci")
print(s1)
# s1 = "Something else"
print(s1)
# Change s4's GPA.
# Cannot do it this way:
# s4.GPA = 2.5
# Can create a whole new Student, with mostly previous values
s4 = Student(s4.name, s4.ID, 2.5, s4.major)
print(s4)
# Can do the same thing with the _replace method
s4 = s4._replace(GPA = 3.75, name="Programmer, Petra")
print(s4)

print("Dewey" in ducks)  
#in is a boolean (check if something is in the sequence)

print(temps)
temps.sort()
print(temps)
print()
print(ducks)
ordered_ducks = sorted(ducks)
print(ducks)
print(ordered_ducks)
temps.sort(reverse=True)
print(temps)

SL = [s1, s2, s3, s4]
print(SL)
SL.sort()
print(SL)

def get_GPA(s: Student) -> float: # ->float what is expected to return
    ''' Return student's GPA '''
    
    return s.GPA
assert s1.GPA == get_GPA(s1)
assert get_GPA(s2) == 3.95

SL.sort(key=get_GPA)
print(SL)
# Can not say:  SL.sort(key=GPA)

"""
Programming languages are EXTENSIBLE
    Data:  e.g., with namedtuples
    Actions:  e.g., by defining our own functions (or methods)


"""

def double(n: int) -> int: #what do we want in the end

    ''' Return twice the parameter'''
    
    return n * 2
assert double(2) == 4
assert double(-18) == -36
assert double(0) == 0

print("Two times 13 is", double(13))
print("Ten percent of that is", double(13) * 0.1)

"""
In the print statement, double(13) is CALLING the function double
    with an ARGUMENT of 13.  The function RETURNS 26, which substitutes
    for the function call in the print statement (and thus gets printed out)
Bare bones version:
    def double(n):
        return n*2
"""
 
