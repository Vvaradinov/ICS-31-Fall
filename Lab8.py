# vvaradin #NOTE: odd numbers in class I couldn't find a partner :(
#Lab 8
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')

print()
print("---c1---")
print()

def read_menu_with_count(file_name: str):
    infile = open(file_name,'r')
    new_list = []
    count = 0
    for obj in infile:
        if count >= 1:
            infile1 = obj.split('\t')
            new_list.append(Dish(infile1[0],float(infile1[1][1:]),int(infile1[2])))
        count += 1
    infile.close()
    return new_list
print(read_menu_with_count('menu1.txt'))


print()
print("---c2---")
print()

def read_menu(file_name: str):
    infile = open(file_name,'r')
    new_list = []
    for obj in infile:
        infile1 = obj.split('\t')
        new_list.append(Dish(infile1[0],float(infile1[1][1:]),int(infile1[2])))
    infile.close()
    return new_list
print(read_menu('menu3.txt'))



print()
print("d")
print()

Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)
  
Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1]) 
StudentBody = [sW, sX, sY, sZ]

print()
print("d1")
print()

def Students_at_level(L: "list of students", class_level: "class level") -> list:
    """ takes list and returns students at class level"""
    new_list = []
    for obj in L:
        if obj.level == class_level:
            new_list.append(obj)
    return new_list
print(Students_at_level(StudentBody,"FR"))

print()
print("d2")
print()

def Students_in_majors(L: "list of students", L_str: "list of strings")-> list:
    """ Takes a list of students and an list of majors and returns the list of students"""
    new_list = []
    for obj in L:
        if obj.major == L_str[1]:
            new_list.append(obj)
    return new_list
    
print(Students_in_majors(StudentBody,['CS','PSB']))



print()
print("d3")
print()

def Students_in_class(L: "list of students", dept: str, conum: str) -> list:
    """ Takes L dept and conum and returns a list of entroled in specific class"""
    new_list = []
    for obj in L:
        if Student_is_enrolled(obj,dept,conum):
            new_list.append(obj)
    return new_list


def Course_equals(c1: Course, c2:Course) -> bool:
    """ Return True if the department and number of c1 match the department and number of c2 ( and False otherwise)"""
    return (c1.dept == c2.dept and c1.num == c2.num)

def Course_on_studylist(c: Course, SL: "list of Course") -> bool:
    """ Return true if the course c equals any course of the list SL (where equality means matching department name and course number and false otherwise) """
    for a_course in SL:
        if Course_equals(c, a_course):
            return True
    return False

def Student_is_enrolled(S: Student, department:str, coursenum: str) -> bool:
    """ Return True if the course (department and course number) is on the student's studylist (and False otherwise) """
    return Course_on_studylist(Course(department,coursenum,'','',0),S.studylist)

print(Students_in_class(StudentBody,'Writing', '39A'))

print()
print("d4")
print()

def Student_names(L: "list of students") -> list:
    """ Take a list of students and return just the names of the students"""
    student_list = []
    for names in L:
        student_list.append(names.name)
    return student_list
print(Student_names(StudentBody))
        

print()
print("d5")
print()
for obj in StudentBody:
    if obj.major in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
        print(obj)


print()
print()

for obj in StudentBody:
    if obj.major in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
        print(obj.name)


print()
print()
count = 0
for obj in StudentBody:
    if obj.major == "ICS":
        count += 1
print(count)

print()
print()
new_list = []
for obj in StudentBody:
    if obj.level == "SR" and obj.major == "ICS":
        new_list.append(obj.name)
print(new_list)

print()
print()
count = 0
for obj in StudentBody:
    if obj.level == "SR" and obj.major == "ICS":
        count += 1
print(count)

print()
print()
count = 0
for obj in StudentBody:
    if obj.level == "SR" and obj.major in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
        count += 1

print(count / 7,'%')

print()
print()
count = 0
for obj in StudentBody:
    if obj.level == "FR" and obj.major in ['CS','CSE','BIM','INFX','CGS','SE','ICS'] and ics31 in obj.studylist:
        count += 1
print(count)

print()
print()
unit_sum = 0
count = 0
for obj in StudentBody:
    for obj1 in obj.studylist:
        if obj.level == "FR" and ics31 in obj.studylist:
            unit_sum +=obj1.units
print(unit_sum / 4)


print()
print()



        
    


        

