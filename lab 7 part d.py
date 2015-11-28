# lab 7
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
