# Quiz 5 
from collections import namedtuple
# Problem 1
Dish = namedtuple('Dish', 'name cuisine phone menu')
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')


def Restaurant_average_calories(R: Restaurant) -> float:
    """Return the average number of calories on the restaurant's menu
    The menu is a list of Dish structures """

    return Menu_average_calories(R.menu)


def Menu_average_calories(M: 'list of Dish') -> float:
    """ Return the average number of calories on the menu ( a list of DISH)"""
    if len(M) == 0:
        return 0
    else:
        sum = 0
        for d in M:
            sum += d.calories
        return d / len(M)

# Problem 2
Student = namedtuple('Student', 'ID name major studylist')
# ALL are strings except studylist, which is a list of courses
# AN example showing the form of the data:
#s1 = Student("11223344", "Anteater, Peter", "FR", "PSB", [ics31, wr39a, bio97, mgt1])


Course = namedtuple("Course", "dept num title instr units")
# ALL strings except number of units
# An example showing the form of the data

#ics31 = Course("ICS", "31", "Intro to Programming", "Kay", 4)

# (a)

def class_level_count(SB: [Student], class_level: str) -> int:  # [STUDENTS] == 'List of students'
    """ Return the number of students in the list SB whose level matches the specified level. """
    result = 0
    for obj in SB:
        if obj.level == class_level:
            result += 1
    return result


# (b)

def inrollments_for_instructor(SB: [Student], instructor_name: str) -> int:
    """ Return the total number of students enrolled in a courses taught by named instructor
    If a student is enrolled in two courses taught by the same instructor, that student counts twice """
    result = 0
    for obj in SB:
        result = result + enrollments_on_studylist(s.studylist, instructor_name)
    return result

def enrollments_on_studylist(courses: [Course], instructor_name: str) -> int:
    """ Return the number of entrollments by this student in courses taught by named instructor"""
    result = 0 # Seperate local variable
    for obj in courses:
        if obj.instr == instructor_name:
            result += 1
    return result

#Problem 3

# (a)

L = ["Huey", "Dewey", "Louie", "Donald", "Daisy"]
for i in range(len(L)):
    print(L[i])


# (b)

Restaurant = namedtuple("Restaurant", "name cuisine phone dish price")
RESTAURANTS = []

def Restaurants_serving_cuisines(RL: [Restaurant], cuisines: [str]) -> [Restaurant]:
    """ Return a list of Restaurants serving any of the cuisines specified"""
    result = []
    for r in RL:
        if r.cuisine in cuisines:
            reuslt.append(r)
    return r
print("Name of south east asian Restaurants")
SEAsian_restaurants = Restaurants_serving_cuisines(RESTAURANTS,
                                                   ['Thai', 'Vietnamese', 'Laotian', 'Cambodian'])
for eeach_rest in SEAsian_restaurants:
    print(each_rest.name)
        
