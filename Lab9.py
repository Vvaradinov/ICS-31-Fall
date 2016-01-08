# vvaradin
from collections import namedtuple
from random import *
NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4


print("--- c.1 ---")

def generate_answers() -> str:
    """ Takes a string and returns random selected answer"""
    a_str = 'AAAAABBBBBCCCCCDDDDD'
    answers = ''
    for obj in a_str:
        answers += choice(a_str)
    return answers      
print(generate_answers())

ANSWERS = "CBACBBBABBCDBBBCBDBA"
print()
print("--- c.2 ---")
print()

Student = namedtuple('Student', 'IDnumber answers')
def random_students() ->list:
    """ Using global constants to generate random student list of namedtuples"""
    IDnumbers = randrange(1,1000000000,2)
    new_list = []
    for obj in range(20): # fix later
        new_list.append(Student(randrange(IDnumbers),(generate_answers())))
    return new_list
print(random_students())

print()
print("--- c.3 ---")
print()
Student = namedtuple('Student', 'ID answers scores total')
def random_students() ->list:
    """ Using global constants to generate random student list of namedtuples"""
    new_list = []
    for obj in range(3):
        IDnumbers = randrange(1,1000000,2)
        correct_num = 0
        score = [randrange(2) for x in range(20)]
        for num in score:
            if num == 1:
                correct_num += 1
        new_list.append(Student(IDnumbers,generate_answers(),score, correct_num))
    return new_list
        
   
print(random_students())


print()
print("--- c.4 ---")
print()
def generate_weighted_student_answer(s: str) -> str:
    """ takes a string (one character, the correct answer) and returns a string
    """
    c_str = 'ABCDCCCCCCCC'
    return choice(c_str)
#print(generate_weighted_student_answer(""))

def random_students2():
    new_list = []
    answer_sheet = ''
    for obj in range(3):
        IDnumbers = randrange(1,1000000,2)
        correct_num = 0
        score = [randrange(2) for x in range(20)]
        for num in score:
            if num == 1:
                correct_num += 1
        new_list.append(Student(IDnumbers,generate_weighted_student_answer("C"),score, correct_num))
    return new_list
                   
print(random_students2())




print()
print("--- d.1a ---")
print()
def calculate_GPA(grades: list)->float:
    '''Returns GPA from grades'''
    GPA = 0
    for grade in grades:
        if grade == 'A':
            GPA += 4
        elif grade == 'B':
            GPA+=3
        elif grade == 'C':
            GPA+=2
        elif grade == 'D':
            GPA+=1
        else:
            GPA += 0
    return GPA/len(grades)

print(calculate_GPA(['A', 'C', 'A', 'B', 'A', 'F', 'D']))

print()
print("--- d.1b --- ")
print()

def calculate_GPA2(grades: list) -> float:
    """ Returns GPA from grades using dict """
    grade_dict = {"A":4, "A-": 3.7, "B+": 3.3, "B": 3.0,"B-": 2.7, "C+": 2.3, "C": 2.0,"C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}
    GPA = 0
    for obj in grades:
        GPA += (grade_dict[obj])
        score = GPA / len(grades)
    return score   
print(calculate_GPA2(['A', 'C', 'A', 'B', 'A', 'F', 'D']))


print()
print("--- d.2 ---")
print()

def flatten_2D_list(L: "2D table list")-> list:
    """ Takes 2D table and returns list"""
    table_2D = [[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]
    return L[0] + L[1] + L[2] + L[3] + L[4]

print(flatten_2D_list([[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]))

print()
print("--- d.3a ---")
print()
L = ['If', 'you', '432234', 'did', 'the', '9834234', 'exercise', 'correctly', '534523423', 
		 'this', 'should', '1044323', 'be', 'readable']

def skip_every_third_item(L: list):
    """ Skips every third item"""
    count = 0
    new_list = []
    for i in range(len(L)):
        count+=1
        if count%3 != 0:
            new_list.append(L[i])        
    return new_list
    
print(skip_every_third_item(L))
print()
print("--- d3b ---")
print()

def skip_every_nth_item(L: list, n: int):
    """ Skips every nth item"""
    count = 0
    new_list = []
    for i in range(len(L)):
        count+=1
        if count%n != 0:
            new_list.append(L[i])        
    return new_list
print(skip_every_nth_item(L, 3))




print()
print("--- d.4a ---")
print()

work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']

def tally_days_worked(L:list) -> dict:
    """ Returns dict where every key is a name of an employee and the value is the number of days worked for a week"""
    workers = {}
    for obj in L:
        if obj == "Bob":
            workers[obj] = L.count("Bob")
        if obj == "Kyle":
            workers[obj] = L.count("Kyle")
        if obj == "Larry":
            workers[obj] = L.count("Larry")
        if obj == "Brenda":
            workers[obj] = L.count("Brenda")
        if obj == "Samantha":
            workers[obj] = L.count("Samantha")
        if obj == "Jane":
            workers[obj] = L.count("Jane")
    return workers
print(tally_days_worked(work_week))

print()
print("--- d.4b --- ")
print()

hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}

def pay_employees(D: "workers", D1: "hourly wages") -> str:
    """ determine how much each employee will be payed """
    work = {}
    for obj in D1 and D:
        work[obj] = (D1[obj] * 8)* (D[obj]) 
    print  ("Samantha will be paid", work["Samantha"]," for,",D["Samantha"], "days of work at", D1["Samantha"], "an hour. \n"
            "Kyle will be paid", work["Kyle"]," for ", D["Kyle"]," days of work at", D1["Kyle"]," an hour. \n"
            "Brenda will be paid", work["Brenda"] ," for ", D["Brenda"], " days of work at", D1["Brenda"]," an hour. \n"
            "Jane will be paid", work["Jane"], " for", D["Jane"],  "days of work at", D1["Jane"], "an hour.\n"
            "Bob will be paid", work["Bob"],  "for", D["Bob"], "days of work at", D1["Bob"]," an hour.\n" 
            "Larry will be paid", work["Larry"], "for",D["Larry"]," days of work at", D1["Larry"], "an hour.")
    
(pay_employees((tally_days_worked(work_week)), hourly_wages))

print()
print("--- d.5 ---")
print()


def reverse_dict(D: dict) -> dict:
    """ reverses the dict and returns a new one"""
    new_dict = {}
    for obj, obj1 in D.items():
        new_dict[obj1] = obj
    return new_dict
print(reverse_dict(hourly_wages))



        
    
    

        
    



   
