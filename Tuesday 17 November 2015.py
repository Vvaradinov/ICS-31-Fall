# ICS 31, Tuesday 17 November 2015, 8 AM


"""
We write programs to model/reflect the real/ outside world.
As we do this, we combine the building blocks our programming lang. gives us:
    Actons: E.g. , new fucntions or methods, control structures, algorithms ...
    Things/objects: int float str bool  lists namedtuples
        List of namedtuples; namedtuples containing lists

        There are other sizes and shapes of data  we can build.
        Python gives us a few more built-in ones.

Object- oriented programming: One popular style of designing programs. #ICS 32

If we choose the right data strucutre, it's a lot easier to write the code.

Today's new shape: Two-dimentional table with rows and columns.
    Normal lists: One number as index, in a straight line [0] to [n].
    Table: Two numbers as index, row and a colum ( row/seat, chair/hour, classroom/hour)
         Contents of table: ticket holder, haircut client, class scheduled/then there
         Build this using list of lists
             A list for the 8:00 clients
             A list for the 9:00 clients
             ....
"""

# On our [monochrome] screen, each pixel is either 0 or 1.

def new_screen(rows: int, columns: int) -> '2D table, list of lists':
    """ Create and return an empty screen:  a list of rows, with each
        row a list of pixels going across that row.  All the pixels
        will be 0 (black).
    """
    result = []
    for r in range(rows):
        result.append([0] * columns)
    return result

assert new_screen(4,2) == [[0,0], [0,0], [0,0], [0,0]]

screen = new_screen(10,5)
print(screen)

def print_screen(s: "2D table, list of lists") -> None:
    """Print screen in matrix from # for black and blank for white
    """
    for row in range(len(s)): #Number of rows
        for col in range(len(s[0])): #number of columns
            if s[row][col] == 0:
                pixel = '#'
            else:
                pixel = ' '
            print(pixel,sep='',end='')   # Print one pixel, no extra parcing
        print()           #Newline at end of loop
    return

print_screen(screen)
print()
screen[2][3] = 1
print_screen(screen)
print()
print()

def set_row(screen: '2D table', rownum: int, value: int) -> None:
    """ Change the screen( in place side effect) so that it
    has the specified value all the way across
    """
    for col in range(len(screen[rownum])):
        screen[rownum][col] = value
    return
set_row(screen, 7, 1)
print_screen(screen)
print()

def set_column(screen: '2D table', colnum: int, value: int) -> None:
    ''' Change the screen (in place, side effect) so the specified column
        has the specified value all the way down
    '''
    for row in range(len(screen)):
        screen[row][colnum] = value
    return

set_column(screen, 1, 1)
print_screen(screen)

"""
We could also write:
    def set_pixel(screen, row, col, value)
    def reverse_pixel(screen,row,col)
        ''' If pixel is 0, make it 1; if it's 1, make it 0 '''
    def draw_rectangle(screen, UL_row, UL_col, LR_row, LR_col)
    def draw_rectangle(screen, UL_row, UL_col, width, height)

More than two dimensions:  "higher dimensionality"
        Three dimensions in space, e.g., for a 3D printer
        Frames of a video: each screen/frame is 2D, then 30 frames/second

        Sequence of 3D points that a robot arm follows in a path:
            position[sequence_number][x][y][z]

        A department store:
            Each row represents a department (men's, women's, furniture, ...)
            Every column is a day of the week (Sunday - Saturday)
            Value of each cell is how much money that department took in
                on that day:  store[dept][day]
            We could open two more branches of the store:
                store[branch][dept][day]
            We could expand to different states
                store[state][branch][dept][day]


DICTIONARIES:  type 'dict' in Python
    Sometimes called tables or maps in other PLs
    A whole new data structure (not lists, not NTs, not strings, ...)
    We use them for two reasons:
        -- Gives us more flexible indexing than lists
            L[num]    (and the number must be in sequence)
            D['Huey'] : The range of keys for indexing is much broader.
        -- The performance of looking something up in a dictionary
            (i.e., ITEM in D) is MUCH BETTER than doing the same thing
            with a list).

Constant lists in Python:
    L = []
    L = ['Huey', 'Dewey', 'Louie']
    L = [r1, r2, r3, r4. r5]

Constant dicts in Python:

"""

D = { }  # Note the curly braces
# Dicts have KEY-VALUE PAIRS
D = { 'Huey': 17, 'Dewey': 23, 'Louie': 32 }
# Keys are restricted (can't be just anything); value can be any data in Python
# Indexing into a dictionary:  What's Dewey's age?
print("Dewey's age is:", D['Dewey'])

"""
Here's the catch:  The "rules" that get you what a dict gives you:
    -- Keys must be an IMMUTABLE type (int, str, tuple, NT; NOT a list]
    -- Values can be anything
    -- Keys must be UNIQUE.  Can't have {'x': 17,  'x': 23}
    -- Order isn't specified.  Python gets to choose what order it
        stores things in.  Nothing stops us from saying sorted(list(D))
    Dictionaries are built using a technique called HASHING, a structure
        called a HASH TABLE.
"""

print(D)
D['Huey'] = 99
print(D)


"""
We also have:
    D.pop(key)  # Remove and return the designated item
"""
print(D.pop('Louie'))
print(D)
"""
    D.update(D2)  # Combine values in D and D2
"""
D.update({'Huey': 15, 'Scrooge': 95, "Daisy": 42})
print(D)

            
            
