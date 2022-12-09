from pprint import pprint


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

    if counter == 5000:
        break

pprint(freq_dict)
        