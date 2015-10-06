#yashv and #vvaradin

#c.1.) Modified code to print dollar sign before every dollar value.
#@param: int
hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = int(input('How many dollars per hour? $'))
print('This many dollars per hour:','$',rate)
print('Weekly salary:','$',hours * rate)

#c.2.)
#param: string, int
#instance fields: variables: newAge is the current age plus one.
#user inputs    : name and age are user input variables.
name = str(input('Hello.  What is your name? '))
print('Hello', name)
print('It\'s nice to meet you')
age = (int(input('How old are you? ')))
newAge = age + 1        
print('Next year you will be', newAge, 'years old')

#d.)
#@param: string, int
#instance fields: variables: kronePerEuro, kronePerDollar, and kronePerBritishPound.
#user inputs:     euros, pounds, and dollars.
print('Please provide this information')
bussinessInfo = str(input('Bussiness name: '))
euros = int(input('Number of Euros: '))
pounds = int(input('Number of Pounds: '))
dollars = int(input('Number of Dollars: '))
#beforementioned is the krone per currency value of different global currencies.
kronePerEuro = 7.46
kronePerBritishPound = 10.33
kronePerDollar = 6.66
print('\n')
print('Copenhagen Chamber Of Commerce')
print('Bussiness name: ', bussinessInfo)
print(euros,'euros is', kronePerEuro * euros,'krone')
print(pounds,'pounds is', kronePerBritishPound * pounds,'krone')
print(dollars,'dollars is', kronePerDollar * dollars,'krone')
print('\n')
print('Total Krone: ', (kronePerEuro * euros) + (kronePerBritishPound * pounds)+ (kronePerDollar * dollars))

#e.)
#Instance fields:   variables: favorite, another, and still_another.
#namedtuple     :   Book
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)
booklist = [favorite, another, still_another]
#e.1
print('The name of the book is:',still_another[0])  
#e.2
print('The price of Memoirs of Sherlock Holmes is $',another[3])
#e.3
#Used method called round to approximate the avergage of the three books to 2 decimal places.
average = round((still_another[3] + another[3] + favorite[3]) / 3,2)
print('The average price of the three books is $',average)

#e.4
#If-Else statement to determine whether given parameter in index is <= or => than the concrete value '1900'.
if(still_another[2] < 1900):
    print(True)
else:
    print(False)
#e.5
#Indexed the value of the still_another array and changed the value.
book1 = still_another[0]
book1 = 26
print('The price of Sherlock Holmes is $',book1)
#e.6
#Percentage taken of the current value stored in the variable book1
newBookPrice = ((20/100)* book1)+ book1
print('The new price of Sherlock Holmes is $',newBookPrice)
#f.)
Animal = namedtuple('Name', 'Species age weight favorite food', ) 
#f.i.)
jumboTheElephant = Animal('Jumbo', 'Elephant',50, 1000, 'Peanuts') 
#f.ii.)
perryThePlatypus = Animal('Perry', 'Platypus', 7, 1.7, 'Shrimp')
#If-Else statement to confirm the value of weight in jumboTheElephant is greater than the value in perryThePlatypus
if(jumboTheElephant[3] > perryThePlatypus[3]):
    print(True)
else:
    print(False)
#g.)
#g.1.)
if(booklist[0].price < booklist[1].price):
    print(True)
else:
    print(False)
#g.2.)
if(booklist[0].year > booklist[-1].year):
    print(True)
else:
    print(False)
#h.)
from collections import namedtuple     # If this line is in your file already, you don't need it again
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
#h.1.)
print('The name of the third restaurant on the list is: ',RC[2].name)
#h.2.)
if(RC[0].cuisine == RC[3].cuisine):
    print(True)
else:
    print(False)
#h.3.)
print('The best dish at the last given restaurant is: ',RC[-1].dish)
#h.4.)
RC.sort()           #Sorts the list alphabetically based on the first items in the restaurant arrays.
print(RC)
print('\n')
#h.5.)
RC.reverse()        #Sorts the list alphabetically in reverse based on the dish items in the given arrays.
print(RC[0].dish)
#h.6.)
RC.sort()
var1 = RC[0].name
var2 = RC[1].name
RC.reverse()        #Sorts the list alphabetically in reverse
var3 = RC[0].name
var4 = RC[1].name
newList = [var1, var2, var3, var4]
print(newList)      #prints the new list with the given parameters

#i
import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=700, height=700)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window
"""
my_canvas.create_line(100, 100, 300, 300, fill='orange') # Draw orange line
my_canvas.create_line(300, 100, 100, 300, fill='blue')   # Draw blue line
tkinter.mainloop()          # Combine all the elements and display the window
"""
#1
my_canvas.create_rectangle(500, 500, 700, 700) 

#2
my_canvas.create_polygon(150, 75, 225, 0, 300, 75, 225, 150, fill="red")
#3
my_canvas.create_rectangle(100, 100, 200, 200, fill = "blue")
#4
my_canvas.create_oval(250, 300, 500, 200, fill = "green")

#Unfortunately this is all we have :(










    


    



    

    







    






