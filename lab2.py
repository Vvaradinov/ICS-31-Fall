# vvaradin


#c
"""
print('How many hours?')
hours = int(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = int(input())
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)

"""
"""
hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = int(input('How many dollars per hour?'))
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)
"""
#c.1
"""
hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = int(input('How many dollars per hour?'))
print('This many dollars per hour:  ', rate, "$")
print('Weekly salary:  ', hours * rate, "$")
"""

#c2
"""

print("Hello. What is your name?")
name = str(input())
print("Hello, Alice Anteater")
print("It's nice to meet you")
print("How old are you")
age = int(input())
print("Next year you will be 20 years old")
print("Good-bye")
"""

#d
"""
krone_per_euro = 7.46
krone_per_pound = 10.33
krone_per_dollar = 6.66
print("Business name:")
busin_name = str(input())
print("Number of euros:")
eur = int(input())
print("Number of pounds")
pounds = int(input())
print("Number of dollars")
dollars = int(input())
print(dollars)

print("Copenhagen Chamber of Commerce")
print("Business name:", busin_name)
print(" 100 euro is", eur * krone_per_euro, "krone")
print(" 200 pounds is", pounds * krone_per_pound, "krone")
print(" 1000 dollars is", dollars * krone_per_dollar, "krone")

print("Total krone:", eur * krone_per_euro + pounds *krone_per_pound +
      dollars * krone_per_dollar)
"""

#e
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)

#e.1
print(still_another.title)
#e.2
print(another.price)
#e.3
print((favorite.price + another.price + still_another.price)/3)
#e.4
print(bool(favorite.year < 1900))
#e.5
still_another = still_another._replace(price = 26)
print(still_another.price)
#e.6
still_another = still_another._replace(price = 26 * (20/100))
print(still_another.price)
#f
Animal = namedtuple('Animal', 'name species age weight food')

animal1 = Animal('Jumbo', 'elephant', 50, '1000kg', 'peanuts')
animal2 = Animal('Perry', 'platapus', 7, '1.7kg', 'shrimp')
print(bool(animal2.weight < animal1.weight))

#g
booklist = [favorite, another, still_another]
#g.1
print(bool(booklist[0] < booklist[1]))
#g.2
print(bool(favorite.year < still_another.year))
#h
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50)]

#h.1
print(RC[2][0])
#h.2
print(bool(RC[0][3] == RC[3][3]))
#h.3
print(RC[6][4])
#h.4
RC.sort()
print(RC)







#i

import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=700, height=700)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

#my_canvas.create_line(100, 100, 300, 300, fill='orange') # Draw orange line
#my_canvas.create_line(300, 100, 100, 300, fill='blue')   # Draw blue line

#tkinter.mainloop()          # Combine all the elements and display the window


#1
#my_canvas.create_rectangle(50, 50, 250, 250)

#2
#my_canvas.create_polygon(150, 75, 225, 0, 300, 75, 225, 150, fill="red")

#3
#my_canvas.create_rectangle(200, 200, 400, 400)

#4
my_canvas.create_oval(100, 150, 300, 100)
my_canvas.create_line(100, 150, 100, 100)
