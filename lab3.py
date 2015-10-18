# vvaradin karinah4

#c.1
def abbreviate(n: str) -> str:
    """ Takes a string and returns it's 3 letter abbreviation"""
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
def create_circle(x: float, y: float, d:float) -> float:
    """ Takes a set of coordinates and diameter and creates a circle"""
    my_canvas.create_oval(x, y, x + d, y + d)
    return
create_circle(100, 200, 300)
create_circle(200, 300, 400)
create_circle(400, 500, 600)
create_circle(200, 500, 400)


#d.1

from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
RC = [Restaurant('Taillevent', 'French', '01-22-33-44-55-66',
                'Escargots', 45.00),
      Restaurant('Chipotle', 'Mexican', '555-5264', 'Burrito', 8.60),
      Restaurant('Thai Dishes', 'Thai', '333-4444', 'Larb Gai', 9.50),
      Restaurant("McDonald's", 'Burgers', '333-4332', 'Big Mac', 3.50)]

def restaurant_price(L):
    """ Takes in an arugment, Restaurant, and returns the price"""
    return L.price
assert restaurant_price(RC[0]) == 45.0
assert restaurant_price(RC[1]) == 8.60
print (restaurant_price(RC[0]))
print (restaurant_price(RC[1]))

print ()

#d.2

"""sorts list of restaurants by price"""
RC.sort(key = restaurant_price)
print (RC)
print()

#d.3

def costliest(R: list) -> str:
    RC.sort(key = restaurant_price, reverse = True)
    return R[0].name
assert costliest (RC) == "Taillevent"
print (costliest(RC))
print()

#d.4

print (RC)
print ()
def costliest2(R: list) -> str:
    sorted(RC, key = restaurant_price, reverse = True)
    return RC[0].name
print(costliest2(RC))

print()


#e
Book = namedtuple('Book', 'author title genre year price instock')
BSI = [Book('James Steward','Air Wars','Fantasy', 1996, 12.50, 50),
       Book('Steward Holms','Core','Sports', 2005, 9.50, 10),
       Book('John Snow','Beware','Fantasy', 2015, 100.00, 50),
       Book('Henry Hill','Technogeek','Technology', 1999, 50.00, 10),
       Book('James Arthur','Superman','Technology', 2001, 45.00, 50)]
#e.1
for item in list(BSI):
    print(item.title)
print()
#e.2
for item in sorted(BSI):
    print(item.title)
print()

#e.3
for item in list(BSI):
    itemincr = item.price + 0.1 * item.price
    print(itemincr)
print()

#e.4
for item in BSI:
    if item.genre == 'Technology':
        print (item.title)
print()

#e.5
Books_before_2000 = ["Air Wars","Technogeek", 60]
Books_after_2000 = ["Core Art of Soccer","Beware","Superman", 110]

if Books_after_2000 > Books_before_2000:
    print("More titles 2000 or later", Books_after_2000[3], "vs", Books_before_2000[2])
else:
    print("More titles 2000 or before")

print()

#e.6
def inventory_value(s: str) -> float:
    """ Takes a book and returns the value of our inventory of that book"""
    return s.price * s.instock
assert inventory_value(BSI[0]) == 625
assert inventory_value(BSI[1]) == 95

print(inventory_value(BSI[4]))
print()

print("The highest value book is", BSI[2].author, "at a value of $", BSI[2].price)


        
    


#f

import tkinter #remove before turning it in
my_window = tkinter.Tk()
my_canvas = tkinter.Canvas(my_window, width= 700, height= 700)
my_canvas.pack()
def create_face(x: float, y: float, w:float, z:float) -> float:
    """ Takes two sets of coordinates and makes the face"""
    my_canvas.create_oval(x, y, w, z, fill='sandy brown')
    return
create_face(0,0,700,700)
def create_eye(x,y) -> None:
    """ Takes a set of coordinates and creates eyes"""
    my_canvas.create_oval(x, y, x + 150, y + 150, fill='white')
    my_canvas.create_oval(x + 25, y + 25, x + 75, y + 75, fill='powder blue')
    my_canvas.create_oval(x + 40, y + 40, x + 60, y + 60, fill='black')
    return
create_eye(150,150)    
create_eye(400,150)
def create_nose(x,y) -> None:
    """Takes a set of coordinates and creates a nose"""
    my_canvas.create_polygon(x, y, x - 40, y + 175, x + 40, y + 175, fill='peru')
    return
create_nose (350,250)
def create_mouth(x,y,w,z) -> None:
    my_canvas.create_arc(x, y, w, z, start=0,extent=-180, fill='black')
    return
create_mouth (200,350,500,600)

