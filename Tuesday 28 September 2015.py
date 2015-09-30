# ICS 31, Tuesday 28 September 2015, 8am

print ("Hello, What's your name")

"""
When we write software, we're modeling the real world

The real world has:
           Things (nouns) Obejcts.
           Actions(verbs) Statements, Operators(* + - /),Function calls
"""
#Two Assignment statements
hours = 40
rate = 10.00
#Print Statement (call the function named 'Print')
print(hours*rate)

"""
STRINGS, or CHARACTER STRINGS
        One type of data.  (Other types are integeres,floats,booleans)
        Strings constant (or 'literals') enclosed in quotation marks.
           'Today is Tuesday'    Apostrophes, single quotes
           "Today is Tuesday"    Double quotes
           '''Today is Tuesday'''     Triple apostrophes
INTEGERS (int)
      Whole numbers, no decimal point   17   -2345
FLOATS, or FLOATING POINT NUMBER (float)
      Numbers that could have a decimal point.   23.45 100.  -.0000000342
BOOLEANS (bool)
      True or False.                     True False   hours == rate
"""

two = """Four score and
seven years ago"""

print(two)

print("""
He said "Hello. What's your name?"
And then he left""")

print("One line\nAdnother line")

#Total bill of a restaurant, with tax and tip.
#   given the base amount of the bill.
print("\n\n\n\n")
print("Hello. What's your name?")
name = input()             #Input function in variable name

print("Hello,", name, ", what's the amount of the total bill?")

TAX_RATE = 0.08        #Symbolic constant

total_bill = float(input())  # Specify numeric/string
print ("I will compute the overall total on $", total_bill, "with tax and tip")
print("What percentage tip would you like to leave?  (15, 18, 20, ....)")
tip_rate = float(input())   #Specify numeric/string

print("Leaving" , tip_rate, "% tip.")

tax_amount = total_bill * TAX_RATE     #Actuall Computation
tip_amount = total_bill * (tip_rate / 100)

print ("The total to pay is",
       total_bill + tax_amount + tip_amount,
       ".")
