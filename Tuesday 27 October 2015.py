# ICS 31, Tuesday 27 October 2015, 8am

from collections import namedtuple
Course = namedtuple('Course', 'dept num title instr units')
# All strings except number of units (float)

ics31 = Course('ICS','31', 'Intro to Programming', 'Kay', 4)
ics32 = Course('ICS','32', 'Programming with Libraries',
               'Thornton', 4)
wr39a = Course('a','b','c','c',5)
bio97 = Course('f','g','h','i',4)
mgt1 = Course('w','x','y','z', 4)

Student = namedtuple('Student', 'ID name level major studylist')
# A studylist is a list of Course objcts

s1 = Student('11223344', 'Anteater, Peter', 'FR', 'PSB',
             [ics31, wr39a, bio97, mgt1])
s2 = Student('22334455', 'Anteater, Andrea', 'SO', 'CS',
             [ics32, wr39a, bio97])

SB = [s1, s2]  # A "Student Body" is a list of Students
SB2 = [s2, s2, s2]
SB3 = [s1, s1, s1, s1]
def num_students(L: 'list of Student') -> int:
    ''' Return number of students in list '''
    return len(L)
assert num_students(SB) == 2
assert num_students([]) == 0

def num_PSB_majors(L: 'list of Student') -> int:
    ''' Return number of PSB majors on list '''
    total = 0
    for s in L:
        if s.major == 'PSB':
            total += 1
    return total
assert num_PSB_majors(SB) == 1
assert num_PSB_majors([]) == 0
assert num_PSB_majors(SB2) == 0
assert num_PSB_majors(SB3) == 4

## We could write num_majors(SB, 'major')
## How many of Major X at Class Level Y are there?
##   E.g., how many sophomore PSB majors?

def num_majors_at_level(L: 'list of Student', maj: str, lev: str) -> int:
    ''' Return the number of specified majors at specified level '''
    total = 0
    for s in L:
        if s.major == maj and s.level == lev:
            total += 1
    return total
assert num_majors_at_level(SB, 'CS', 'SO') == 1
assert num_majors_at_level(SB, 'CSE', 'SO') == 0
assert num_majors_at_level(SB, 'CS', 'SR') == 0
assert num_majors_at_level(SB3, 'PSB', 'FR') == 4

# Total number of course enrollments (total seats occupied, all classes)
def num_bodies_in_seats(L: 'list of Student') -> int:
    ''' Return number of enrollments, all students, all classes '''
    total = 0
    for s in L:
        total += len(s.studylist)
    return total
assert num_bodies_in_seats(SB) == 7

# Total number of units enrolled for a student.
def units_enrolled(s: Student) -> float:
    ''' Return total number of units for this student '''
    total = 0
    for c in s.studylist:
        total += c.units
    return total
assert units_enrolled(s1) == 17

def total_units_enrolled(L: 'list of Student') -> float:
    ''' Return total units enrolled for whole student body '''
    total = 0
    for s in L:
        total += units_enrolled(s)
    return total
assert total_units_enrolled([s1]) == 17
assert total_units_enrolled(SB) == 30

## This is better than one function with nested for-loops
## because it gives us interchangeable parts.  But try to write
## the nested-loop version, too.

## Average units per student?

## Number of CS, CGS, CSE, BIM, Infx, SE majors:
## One approach:  for m in ['CS', 'CGS', ...]:   and add results.
## Another approach:  if s.major in ['CS', 'CGS', ...]:  add 1 to total.


## TEXT PROCESSING

'''
A string is made up of (zero or more) CHARACTERS.
A character is any keystroke: letter, digit, punctuation, space, tab
Zero characters is the EMPTY STRING:   x = ''  or  x = ""
    len(s)     in     for c in s:   indexing:  s[3]  slices:  s[3:7]
WHITE SPACE characters are space, tab, newline/return
'''
s = 'Donald Duck'
print(s[0:3])
# Defaults with slices
print(s[:4])
print(s[4:])
print(s[::3]) # Every third character

## Constant strings are DELIMITED by single-quotes, double-quotes,
##    triple-quotes

## STRING METHODS

print("Where does the first 'on' occur in s?")
print(s.find('on'))
print("'ld' is at", s.find('ld'))
print(s.find('one'))  ## Not there?  Returns -1

print("Does s start with an H?", s.startswith('H'))
print("Does s start with Don?", s.startswith('Don'))
# Also s.endswith()

print("How many times does 's' occur in 'Mississippi'?",
      'Mississippi'.count('s'))
print("How many times does 'ss' occur in 'Mississippi'?",
      'Mississippi'.count('ss'))

m = 'Mississippi'
print("Change all the 's'-es to 'ok' in 'Mississippi':",
      m.replace('s', 'ok'))
print(m)

## UPPER CASE (capital) and LOWER CASE (small) letters
print(m.upper())
print(m.lower())
print(m)
