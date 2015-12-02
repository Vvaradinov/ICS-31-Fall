# QUIZ 6
print()
print("--- 1A ---")
print()
counts = [1, 0, 0, 2, 2, 3, 8, 22, 33, 40, 45]
TOPSCORE = 10
for s in range(TOPSCORE + 1):
    print("{:2d}. {:3d} ({:5.2f}%)".format(s, counts[s], counts[s]/sum(counts)*100))


print()
print("--- 1B ---")
print()
for s in range(TOPSCORE + 1):
    print("{:0d}. {:3d} ({:.2f}%) {}".format(s, counts[s], counts[s]/sum(counts)*100, "*" * counts[s]))

print()
print("--- 2 ---")
print()

def seconds_to_mmss(seconds: int) -> str:
    """ Convert a number of seconds to minutes and seconds in "mm:ss" format """
    return str(seconds//60) + ":" + str(seconds % 60)
print(seconds_to_mmss(3620))
    

assert(seconds_to_mmss(15) == "0:15") 
assert(seconds_to_mmss(75) == "1:15") 
assert(seconds_to_mmss(3620) == "60:20")

print()
print("--- 3 ---")
print()

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
def mmddyy_to_MonthDayYear(mmddyy: str) -> str:
    ''' From an argument in the form '10/31/152' (month, day, year),
    return a string in the form 'October 31, 2015'. Assume all
    values are valid numbers and all years are in this century
    (that means your function doesn't have to check).
    '''
    fields = mmddyy.split('/')
    month_number = int(fields[0]) - 1 
    month_name = MONTHS[month_number]
    day = fields[1] 
    year = '20' + fields[2] 
    return month_name + " " + day + ", " + year
print(mmddyy_to_MonthDayYear('10/31/16'))

assert(mmddyy_to_MonthDayYear('10/31/15') == 'October 31, 2015')
assert(mmddyy_to_MonthDayYear('12/1/07') == 'December 1, 2007')
assert(mmddyy_to_MonthDayYear('1/3/99') == 'January 3, 2099')

print()
print("--- 4 ---")
print()
def remove_front_matter(linelist: [str]) -> [str]:
    ''' Return input list with starting lines (through "END OF FRONT MATTER") removed
    '''
    dividing_line = 0
    for line_obj in linelist:
        if line_obj == "END OF FRONT MATTER":
            break
        dividing_line += 1
    return linelist[dividing_line + 1 :]
test_list = ["To be skipped",
 "Also to be skipped",
 "END OF FRONT MATTER",
 "To be included",
 "Also to be included"]

print(remove_front_matter(test_list))

assert(remove_front_matter(test_list) == ["To be included",
 "Also to be included"])
assert(remove_front_matter(test_list[2:]) == ["To be included",
 "Also to be included"])
assert(remove_front_matter(test_list[:3]) == [ ])

print()
print("--- 5a ---")
print()

quiz_scores = [18, 20, 18, 20, 0, 10, 10, 20, 10, 20]
quiz_counts = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 4]

def zero_counts(top_value: int) -> 'list of int':
    '''Return a list of zeroes, with one zero for each possible score from zero to top_value '''
    result = []
    for obj in range(top_value + 1):
        result.append(0)
    return result
print(zero_counts(10))


print()
print("--- 5c ---")
print()
def count_scores(scores: 'list of int', top_score: int) -> 'list of int':
    ''' Return a list that tallies the number of times each value (from 0
    to top_score) occurs in the list of scores
    '''
    counts = zero_counts(top_score)
    for s in scores:
        counts[s] += 1
    return counts
print(count_scores(quiz_scores, 20))
