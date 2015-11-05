# ICS 31, Tuesday 3 November 2015, 8am

"""
FILES : Give us PERSISTENCE: Data sticks around from
    one run of the program to the next.

New features of programming languages:
    Some let you solve new kinds of problems, like lists.
    Some( just ) let you do the same things more conveniently.
        for i in range(10):
           --- body of loop
        ** can be rewritten as **
        i = 0
        while i < 10:
            --- body of loop
            i += 1
        ** We could call a foor-loop "SYNTACTIC SUGAR"
        EQUIVELENT FOR LOOP == WHILE LOOP
Files are in the new-problems-solved category.

We read from files. 
We write to files.
Files come in alot of different forms:
    "File name extensions"
        .xls, .doc, .pdf, .py, .pq, ....
    We're just going to deal with plain TEXT files
        (sometimes called ASCII  with exstension .txt)
        ASCII is the standard correspondence
            bits (1s and 0s) and keystrokes/characters
    File: a document.
    Directory:   a folder containing documents
    File system: A collection of all the folders on the computer
    We are going to deal with reading and writting files in the same folder
        in the same foler as our .py file



Basic steps of file i/o ("i/o" stands for input and output)
    1. Open the file. Like dialing the phone number: stars with the
          connection between your program and the file on the disk
          (and the operating system)
          Choose: Open for reading, open for writting to it
          We open a file once at the start of the program,
              before we read anything from it or write anything to it
    2. Read the datta from the file/ write the data to it 
    3. Close the file
           Just do this once per file.
"""

infile = open('Something.txt', 'r') # calls a text file in the same folder where py file is
# open(" FILE NAME ", "R" - READ)

data = infile.read() # .read() - READING FROM THE FILE ONLY
##print(data)
#Alternative: Create a list of individual lines in the file
datalines = data.split("\n") # splits to a list
print(datalines)
for i in range(len(datalines)):
    print("Line number", i,".   ", datalines[i])
    

infile.close() # .close () CLOSES THE FILE SO WE CANT EDIT IT


outfile = open('new-Something.txt', 'w') #Makes a new txt file and writes something in ti
outfile.write(data) # .write() method writes things in the new file
outfile.close()




"""
Four ways to read data from files:

1.  read() method.  Reads the whole file into one big string.
    Good for when we want to process the whole thing at once,
    e.g., to eliminate punctuation.
    Downsides:  (a) A really huge file mght not fit into memory
        all at once.
        (b) You have to do all the processing (split it into
        lines or words or whatever.  There are alternatives that
        do some of that work for you.

1a. read(n) method:  Read the next n characters from the input.
    Useful for data that comes in a fixed format:
        Escargots         23.50   495  "I really liked this dish.  --Frenchy"
        Blanc de veau     45.00   550
        Oeufs a la neige  17.95   960
    read a line:  name = infile.read(18)
                  price = float(infile.read(5))
                  calories = int(infile.read(6))
                  restofline = infile.readline()

2.  readline() method.  Read everything from the current position
        to the next \n (or the end of the file, 'EOF').
        If nothing left to read, it returns the empty string.
    Useful for really huge files, or any time you need to:
        read a line
        process it
        repeat

3.  readlines() method.  Reads all the lines in the file into a list.
        (We did this above with read() and split("\n").)

4.  for a_line in infile:
        # Do whatever you want with the variable a_line

    E.g., to copy a file line by line:
    # Open both files:
    infile = open('orig.txt', 'r')
    outfile = open('copy.txt', 'w')
    for line in infile:
        # We could add any processing of a_line here
        outfile.write(line + "\n")
    infile.close()
    outfile.close()

""" 
