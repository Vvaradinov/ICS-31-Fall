# Quiz 7

print()
print("Problem 1")
print()

test_list = ["To be skipped",
 "Also to be skipped",
 "END OF FRONT MATTER",
 "To be included",
 "Also to be included"]


def remove_front_matter(linelist: "list of str") -> "list of str":
    """ Return input list with starting lines (through "End  OF FRONT MATTER") removed
    """
    dividing_line = 0
    for line_obj in linelist:
        if line_obj == "END OF FRONT MATTER":
            break
        dividing_line += 1
    return linelist[dividing_line + 1: ]
print(remove_front_matter(test_list))


print()
print("Problem 2")
print()

from collections import namedtuple
Date = namedtuple('Date', 'year month day')
""" All 3 field are numbers """
DrivingRecord = namedtuple('DrivingRecord', 'name license age tickets')
""" name is string, license is string, age is int, tickets is list of Date objects containing the dates of which the driver had the ticket """

print()
print("a")
print()

def Date_is_earlier(date1: Date, date2: Date) -> bool:
    """Return True if date1 is earlier than date2 (and False otherwise---
    for a boolean function, this goes without saying; it has to return
    either True or False)"""
    if date1 < date2:
        return True
    else:
        return False
    

print(Date_is_earlier(Date(2017,1,1), Date(2013,1,1)))


print()
print("b")
print()

def total_tickets(DRL: 'list of DrivingRecord') -> int:
    total = 0
    for dr in DRL:
        total += len(dr.tickets)
    return total

def total_weekend_tickets(DRL: 'list of DrivingRecord') -> int:
    total = 0
    for dr in DRL:
        total += total_weekend_tickets_on_list(dr.tickets)
    return total

def total_weekend_tickets_on_list(ticketlist: 'list of Date') -> int:
    total = 0
    for obj in ticketlist:
        if Date_is_weekend(obj):
            total += 1
    return total

def weekend_ticket_percentage(DRL: 'list of DrivingRecord') - float:
    return total_weekend_tickets(DRL) / total_tickets(DRL) * 100


print()
print("Problem 3")
print()

print('a')



print("b")
def DRList_to_file(DRL: 'list of DrivingRecord', filename: str) -> None:
    outfile = open(file_name, 'w')
    for dr in DRL:
        output_line = dr.name + "\t" + str(dr.license) + "\t" + str(dr.age) + "\t"
        for obj in dr.tickets:
            output_line += Date_to_mmddyy(d) + ","
        output_line = output_line[:-1] + "\n"
        outfile.write(output_line)
    outfile.close()
    

