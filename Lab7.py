# vvaradin #samo

from random import randrange
from random import choice

print()
print("--- c.1 c.2 c.3 ---")
print()

def random_names(n: int) -> list:
    """Takes an int and returns a list of the names"""
    for something in range(n):
        sur_name = single_random_name(datalist2)
        female_name = single_random_name(datalist1)
        male_name = single_random_name(datalist)
        boy_or_girl = choice([male_name, female_name])
        print([sur_name, boy_or_girl])
   
    return


infile = open("malenames.txt", "r")
infile1 = open("femalenames.txt", "r")
infile2 = open("surnames.txt", "r")
data = infile.read()
data1 = infile1.read()
data2 = infile2.read()
datalist = data.split()
datalist1 = data1.split()
datalist2 = data2.split()
    
def single_random_name(L: "list of all the names") -> list:
    """Return list of surnames """
    new_list = L[0::4]
    random_index = randrange(0,len(new_list))
    return new_list[random_index]

(random_names(5))


print('---------------part d-----------------')
print()
print()
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def rotate_alphabet(numb2: int)->str:
    alph_obj = ((ALPHABET + ALPHABET[:numb2%26]))
    return alph_obj

   
def Caesar_encrypt(s: str, numb: int):
    alph_obj = rotate_alphabet(numb)
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', alph_obj[numb%26:])
    return s.translate(table)

print(Caesar_encrypt('hello my name is vladimir putin', 31))

def Caesar_decrypt(d: str, numb2: int):
    alph_obj = rotate_alphabet(numb2)
    table = str.maketrans(alph_obj[numb2%26:], 'abcdefghijklmnopqrstuvwxyz')
    return d.translate(table)

print(Caesar_decrypt(Caesar_encrypt('hello my name is Vladimir Putin', 5), 5))

def strip_punctuation(word:str)->str:
    result = ""
    punctuation = ",.?!:;-()_[]/{}<> "
    for obj in word:
        if obj not in punctuation:
            result += obj
    return result

infile = open('wordlist.txt')
dictionary = infile.read()
infile.close()

def Caesar_break(cipher:str) -> str:
    alph_obj = cipher.split()
    for obj in range(len(temp)):
        alph_obj[obj] = strip_punctuation(alph_obj[i])
    top_count = 0
    match = 0

    for x in range(26):
        count = 0
        for a in temp:
            if Caesar_decrypt(a, x) in dictionary:
                count += 1
        if count >= top_count:
            top_count = count
            match = x
    return Caesar_decrypt(cipher, match)
print('---------------part d.2-----------------')
print()
print()
def Caesar_break(cipher:str) -> str:
    temp = cipher.split()
    for i in range(len(temp)):
        temp[i] = strip_punctuation(temp[i])
    top_count = 0
    match = 0

    for i in range(26):
        count = 0
        for n in temp:
            if Caesar_decrypt(n, i) in dictionary:
                count+=1
        if count >= top_count:
            top_count = count
            match = i
    return Caesar_decrypt(cipher, match)
print(Caesar_break('mjqqt rd sfrj nx aqfinrw'))

print('------e.1------')

def copy_file():
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()


print('------e.2------')

def copy_file(LN: str ):
  infile_name = input("Please enter the name of the file to copy: ")
  infile = open(infile_name, 'r', errors='ignore')
  outfile_name = input("Please enter the name of the new copy:  ")
  outfile = open(outfile_name, 'w')
  if LN == 'line numbers':
      number = 0
      for line in infile:
          number+=1
          LNline = ("{:6d}: {:}".format(number, line))
          outfile.write(LNline)
        
  else:
      for line in infile:
        outfile.write(line)
  infile.close()
  outfile.close()

copy_file('line numbers')

print('------e.3------')

def copy_file(gt: str ):
  infile_name = input("Please enter the name of the file to copy: ")
  infile = open(infile_name, 'r')
  outfile_name = input("Please enter the name of the new copy:  ")
  outfile = open(outfile_name, 'w')
  if gt == 'Gutenberg trim':
      omit = True
      for line in infile:
          if "*** START" in line:
              omit = False
          if "*** END" in line:
              outfile.write(line)
              break
          if omit is False:
                outfile.write(line)        
  else:
      for line in infile:
        outfile.write(line)
  infile.close()
  outfile.close()


print('------e.4------')

def stat(info: [str]) -> str:
    result =''
    result += "{0:5}    {1:}".format(len(info), "lines in the file") + '\n'
    result += "{0:5}    {1:}".format(info.count('\n'), "empty lines") + '\n'
    
    total = 0
    for i in info:
        total += len(i)
    averagechar = total / len(info)
    averagechar_nonempty = total / (len(info) - info.count('\n'))
    
    result += "{0:8.2f} {1:}".format(averagechar, "average characters per line") + '\n'
    result += "{0:8.2f} {1:}".format(averagechar_nonempty, "average characters per non-empty line")
    return result

def copy_file(stat:str):
  infile_name = input("Please enter the name of the file to copy: ")
  infile = open(infile_name, 'r')
  outfile_name = input("Please enter the name of the new copy:  ")
  outfile = open(outfile_name, 'w')
  filelist = infile.readlines()
  if stat == 'statistics':
      statinfo = open(infile_name, 'r')
      statlist = statinfo.readlines()
      for line in infile:
          outfile.write(line)
      print(stat(statlist))
  else:
      for line in infile:
        outfile.write(line)
  infile.close()
  outfile.close()
