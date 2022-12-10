from pprint import pprint

"""
This python module reformats the password according to this rule
Rule:
    IF CHAR IS UPPER_CASE_LETTERS = L
    IF CHAR IS LOWER_CASE_LETTERS = l
    IF CHAR IS DIGITS/NUMBERS = d
    IF CHAR IS A SPECIAL_CHARACTER = s
According to the above rules we will reformat the passwords and
calculate the frequency
"""


file = open('passwords.txt','rb')
freq_dict = {}
counter = 0
for i in file:
    i = str(i).replace("b'",'').replace("\\n'",'')
    temp = list(i)
    for j in temp:
        if j.isalpha() and j.islower():
            temp = list(map(lambda x: x.replace(j, 'l'), temp))
        elif j.isalpha() and j.isupper():
            temp = list(map(lambda x: x.replace(j, 'L'), temp))
        elif j.isdigit:
            temp = list(map(lambda x: x.replace(j, 'd'), temp))
        elif j in ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']:
            temp = list(map(lambda x: x.replace(j, 's'), temp))
    
    k = "".join(temp)
    if k not in freq_dict:
        freq_dict[k] = 1
    else:
        freq_dict[k] += 1
    
    counter += 1

    # This is a termination condition for testing purposes only
    # The code was taking a long time to execute
    if counter == 5000:
        break

pprint(freq_dict)
        