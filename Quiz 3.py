"""
function2
function1
function3
function4

Donald
Huey
Dewey
Louie

Dewey
Louie


Mouse
Pluto

Nephews
Huey 
Dewey 
Louie 
Uncle Donald


Election years
0 -- 2004
1 -- 2008
2 -- 2012
3 -- 2016
Remember to vote!
"""

def abbr(s: str, s1: str) -> str:
    """ Takes 2 strings and returns 2 letter abbreviaton """
    return (s[0:1]) + (s1[0:1])
assert abbr("University", "California") == "UC"
assert abbr("United", "States") == "US"

print(abbr("Star", "Craft"))



from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
RC = [Restaurant('Taillevent', 'French', '01-22-33-44-55-66',
                'Escargots', 45.00),
      Restaurant('Chipotle', 'Mexican', '555-5264', 'Burrito', 8.60),
      Restaurant('Thai Dishes', 'Thai', '333-4444', 'Larb Gai', 9.50),
      Restaurant("McDonald's", 'Burgers', '333-4332', 'Big Mac', 3.50)]

def Restaurant_price(L: Restaurant) -> float:
    return L.price




def least_expensive(R: list) -> float:
    RC.sort(key = Restaurant_price)
    return R
print(least_expensive(RC))



Image = namedtuple('Image', 'height width content')
image1 = Image(250, 150, "w")
image2 = Image(150, 250, "x")
image3 = Image(100, 100, "y")
image4 = Image(1500, 1000, "z")
image_list = [image1, image2, image3, image4]

#(a)
def is_portrait(i: Image) -> bool:
    """ Return true if image is portait-style and False otherwise"""
    if i.height > i.width:
        return True
    else:
        return False

       


assert is_portrait(image1)
assert not is_portrait(image2)
assert not is_portrait(image3)

print(is_portrait(image1))
print(is_portrait(image2))
print(is_portrait(image3))
print(is_portrait(image4))


def keep_portraits(L: 'list of Image') -> 'list of Image':
    """Extract portrait style img from parameter, returning them to a list"""
    result = []
    for i in L:
        if i.height > i.width:
            result.append(i)
    return L
            



print(keep_portraits())
         
             
         


    
    
    
