# vvaradin karinah4

#c.1
def abbreviate(n: str) -> str:
    """ Takes a string and returns it's first 3 letter abbreviation"""
    print(n[0:3])
    return (n[0:3])                     
assert abbreviate('January') == 'Jan'
assert abbreviate('April') == 'Apr'
assert abbreviate('Vladislav') == 'Vla'
assert abbreviate('Karina') == 'Kar'

abbreviate('January')
print()

#c.2
def find_area_square(n: int) -> int:
    """ Takes a side of a square and returns it's area"""
    print(n * n)
    return (n * n)
assert find_area_square(1) == 1
assert find_area_square(5) == 25
assert find_area_square(10) == 100

find_area_square(12)
print()

#c.3
def find_area_circle(n: float) -> float:
    """ Takes the radius and returns the area"""
    pi = 3.14159
    print(pi * (n**2))
    return(pi * (n**2))
assert find_area_circle(1) == 3.14159
assert find_area_circle(5) == 78.53975
assert find_area_circle(10) == 314.159

find_area_circle(15)
print()

#c.4
L = [2, 47, 31, 99, 20, 19, 23, 105, 710,1004]
""" Takes a list and prints all even numbers"""
for x in list(L):
    if x % 2 == 0:
        print(x)
print()

#c.5
def calculate_shipping(n: float) -> float:
    """ Takes the weight and returns cost of shipping"""
    if n < 2.00:
        return(2.00)
    elif n < 10:
        return(5.00)
    else:
        n >= 10
        s = n - 10
        return (5.00 + (s * 1.5))

assert calculate_shipping(1.5) == 2
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 12.5
assert calculate_shipping(20) == 20.00
assert calculate_shipping(100) == 140.0
print(calculate_shipping(35))
print()

#c.6

import tkinter
my_window = tkinter.Tk()
my_canvas = tkinter.Canvas(my_window, width= 700, height= 700)
my_canvas.pack()
def create_square(x: float, y: float, l: float) -> float:
    """ Takes one set of coordinates and lenght and creates a square"""
    my_canvas.create_rectangle(x, y, x + l, y + l)
    return
create_square(100, 200, 300)
create_square(200, 300, 400)
create_square(400, 500, 600)
create_square(200, 500, 400)

#c.7
my_window = tkinter.Tk()
my_canvas = tkinter.Canvas(my_window, width= 700, height= 700)
my_canvas.pack()
def create_circle(x: float, y: float, d: float) -> float:
    """ Takes one set of coordinates and diameter and create a circle"""
    my_canvas.create_oval(x, y, x + d, y + d)
    return
create_circle(100, 200, 300)


#d












          

    
