#ICS 31, Thursday 1 October 2015 8am


print("""Hello
Good-bye
Hello again.""")


"""
This triple-quoted sting is an annotation.
We don't tell Python to do anything with it (assing, print, ...)
so it just sits here for human readers

"""

"""
Things (nouns) CS term is OBJECTS
    int        float        str         bool  (Boolean, George Boole, True/False)
    -17        3.143434    'Hello'     True

    We can combine these values into EXPRESSIONS:
           17
           17 + 3.17
           'Hello' * 3

    We can combine them to describe more complex data (namedtuples)

Actions (verbs): Statements  Function calls  Operators    Method calls
    Statements:  assignment statement
                 name = 'Daffy Duck'
    Function call:
                 print(a,b,c)
                 Predefined functions     sqrt(x)     len(L)

    Operators:   + - * /     %(mod)   numbers


"""
from math import sqrt
x = 25
y = sqrt(x)
print(y)



"""
Things//nouns/objects
    Single-valued data (int, float, bool, str)
    Multiple-valued data: str
       LISTS:   Collections of the same type of thing
            L = [ 89, 92, 92, 91, 88 , 95]
            print(L, len(L))
       NAMETUPLES:   Packaging multiple components of the same thing
           (more omplex) objects, like a student with name, GPA, year of birth
          E.g., a stdent has a name in ID a GPa, a year of birth & a major

"""

L = [ 89, 92, 92, 91, 88 , 95]
print(L, len(L))
nephews = ['John', 'Boby', 'Stewie']
print(nephews)
print(len(nephews))

# Two plain tuples that (each) describe a student:
s1 = ('Jones, John', 33334444, 3.55, 1996, "CSE" )
s2 = ('Smith, Jane', 11122233, 3.65, 1997, "CS" )



"""
INDEXING: Specifying, by number, which part of a mtlti-item object

"""
print("First item in L is:", L[0])
# ZERO-BASED INDENXING: The first item in a list is 0
print(L[5])


#Can get the pieces/ components/ FIELDS out of a tuple by indenxing
print("S1's name is", s1[0])

#NAMEDTUPLES are more conviniet than plain tuples

##USING A NAMEDTUPLE

#Step 1: Set it up(say this once at the top of the program)
from collections import namedtuple

#Step 2: Define what your object looks like
#   A student has a name, ID, GPA, year of birth, major

Student = namedtuple('Student', 'name ID GPA birth_year major')

#Step 3: Create a couple of objects of this new type

student1 = Student("Jones, John", 33334444, 3.55, 1996, "CSE")
student2 = Student("Smith, Jane", 11122233, 3.65, 1997, "CS")

#Step 4: Use these objects; refer to FIELDS as needed with dots
print(student1)
print(student1.name , "was born in", student1.birth_year, "majoring in",
      student1.major, "with GPA", student1.GPA)

#student1.name = "Smith, Sam"     ## NO GOOD: ERROR

student1 = Student("Smith, Sam", student1.ID, student1.GPA,
                   student1.birth_year, student1.major)

print(student1.name, "was born in", student1.birth_year, "majoring in",
      student1.major, "with ID", student1.ID)

print(student2.name , "was born in", student2.birth_year, "majoring in",
      student2.major, "with ID", student2.ID)
student2 = student2._replace(ID = 44445555)
## student2._replace(ID = 44445555)  ### CANT SAY IT LIKE THIS
print(student2.name , "was born in", student2.birth_year, "majoring in",
      student2.major, "with ID", student2.ID)


print(L + [99])                   
                   
        


