import json
from pprint import pprint


possible_password_list = []
matched_passwords = []

def find_combinations(ip_list):
    for i in range(3,16):
        for j in range(0,3):
            parse_list(ip_list,i,j)


def find_interstion_with_data():
    global possible_password_list
    global matched_passwords
    file = open('passwords.txt','rb')
    for i in file:
        i = str(i).replace("b'",'').replace("\\n'",'')
        if i in possible_password_list:
            print("Match found",i)
            matched_passwords.append(i)

def parse_list(ip_list,no_of_chars,skip_chars):
    global possible_password_list
    if skip_chars != 0:
            for i in range(0,len(ip_list)):
                if i > (len(ip_list) - no_of_chars):
                    break
                counter = 0
                j = i
                res_str = ''
                while counter != no_of_chars:
                    if j >= len(ip_list):
                        break
                    res_str += ip_list[j]
                    j += (skip_chars+1)
                    counter += 1
                if len(res_str) == no_of_chars:
                    # print("\nPossibility",i)
                    # print(res_str)
                    possible_password_list.append(res_str)
                
    else:
        for i in range(0,len(ip_list)):
            if i > (len(ip_list) - no_of_chars):
                break
            counter = 0
            j = i
            res_str = ''
            # print("\nPossibility",i)
            while counter != no_of_chars:
                res_str += ip_list[j]
                j += 1
                counter += 1
            # print(res_str)
            possible_password_list.append(res_str)

keyboard_dict = {} 
"""
Data set format => '3a':{3: []} here 
the main root element in the dictionary is 3a and it can be represented as 3 -> skip chars and 'a' -> chars
"""
parse_stack = []

possible_patterns_data_set = {}

upper_end_keys = ['1','2','3','4','5','6','7','8','9','0','-','=','!','@','#','$','%','^','&','*','(',')','_','+']
lower_end_keys = ['z','x','c','v','b','n','m',',','.','/','Z','X','C','V','B','N','M','<','>','?']
left_end_keys = ['1','q','a','z','!''Q','A','Z']
right_end_keys = ['=','\"',"'",'/','+','|','"','?',"\\"]

last_keys = ['~','`','\\','|']


# This loads the keyboard data stored in the keyboard.json file
def load_keyboard_data():
    global keyboard_dict
    keyboard_json = open('keyboard.json')
    temp = json.load(keyboard_json)
    print("Initialized the keyboard data!")
    keyboard_dict = temp


def find_end_keys(direction,intermediate_char):
    global keyboard_dict
    global lower_end_keys

    temp = intermediate_char
    if direction == 'UP' or direction == 'UP-R':
        if str(temp).islower():
            while True:
                temp = keyboard_dict[temp]['down']
                if temp in lower_end_keys:
                    break
        else:
            while True:
                temp = keyboard_dict[temp]['shift_down']
                if temp in lower_end_keys:
                    break

    elif direction == 'DOWN' or direction == 'DOWN-R':
        if str(temp).islower() or str(temp).isnumeric() or str(temp) in ['[',']','\\',';',"'",',','.','/','-','=']:
            while True:
                temp = keyboard_dict[temp]['up']
                if temp in upper_end_keys:
                    break
        else:
            while True:
                temp = keyboard_dict[temp]['shift_up']
                if temp in upper_end_keys:
                    break
    elif direction == 'RIGHT':
        if str(temp).islower() or str(temp).isalnum() or str(temp) in ['[',']','\\',';',"'",',','.','/','-','=']:
            while True:
                temp = keyboard_dict[temp]['left']
                if temp in left_end_keys:
                    break
        else:
            while True:
                temp = keyboard_dict[temp]['shift_left']
                if temp in left_end_keys:
                    break
    
    elif direction == 'LEFT':
        if str(temp).islower() or str(temp).isalnum() or str(temp) in ['[',']','\\',';',"'",',','.','/','-','=']:
            while True:
                temp = keyboard_dict[temp]['right']
                if temp in left_end_keys:
                    break
        else:
            while True:
                temp = keyboard_dict[temp]['shift_right']
                if temp in left_end_keys:
                    break
    return temp


def generate_keyboard_patters(initial_character,direction,n):
    global keyboard_dict
    global parse_stack

    parse_stack.append(initial_character)
    temp = initial_character

    if direction == 'DOWN':
        upper_char = find_end_keys(direction,initial_character)
        for i in range(1,n):
            if str(initial_character).islower() or str(initial_character).isnumeric()  or str(initial_character) in ['[',']','\\',';',"'",',','.','/','-','=']:
                # print(temp)
                if keyboard_dict[temp]['down'] == upper_char:
                    temp = keyboard_dict[temp]['diag_down_right']
                    parse_stack.append(temp)
                    upper_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['down'])
                    temp = keyboard_dict[temp]['down']
            else:
                # print(temp)
                if keyboard_dict[temp]['shift_down'] == upper_char:
                    temp = keyboard_dict[temp]['shift_diag_down_right']
                    parse_stack.append(temp)
                    upper_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['shift_down'])
                    temp = keyboard_dict[temp]['shift_down']
    
    elif direction == 'UP':
        lower_char = find_end_keys(direction,initial_character)
        for i in range(1,n):
            if str(initial_character).islower():
                if keyboard_dict[temp]['up'] == lower_char:
                    temp = keyboard_dict[temp]['diag_up_right']
                    parse_stack.append(temp)
                    lower_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['up'])
                    temp = keyboard_dict[temp]['up']
            else:
                if keyboard_dict[temp]['shift_up'] == lower_char:
                    temp = keyboard_dict[temp]['shift_diag_up_right']
                    parse_stack.append(temp)
                    lower_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['shift_up'])
                    temp = keyboard_dict[temp]['shift_up']
        
    elif direction == 'UP-R':
        lower_char = find_end_keys(direction,initial_character)
        for i in range(1,n):
            if str(initial_character).islower():
                if keyboard_dict[temp]['up'] == lower_char:
                    temp = keyboard_dict[temp]['diag_up_left']
                    parse_stack.append(temp)
                    lower_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['up'])
                    temp = keyboard_dict[temp]['up']
            else:
                if keyboard_dict[temp]['shift_up'] == lower_char:
                    temp = keyboard_dict[temp]['shift_diag_up_left']
                    parse_stack.append(temp)
                    lower_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['shift_up'])
                    temp = keyboard_dict[temp]['shift_up']

    
    elif direction == 'DOWN-R':
        upper_char = find_end_keys(direction,initial_character)
        for i in range(1,n):
            if str(initial_character).islower():
                if keyboard_dict[temp]['down'] == upper_char:
                    temp = keyboard_dict[temp]['diag_down_left']
                    parse_stack.append(temp)
                    upper_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['down'])
                    temp = keyboard_dict[temp]['down']
            else:
                if keyboard_dict[temp]['shift_down'] == upper_char:
                    temp = keyboard_dict[temp]['shift_diag_down_left']
                    parse_stack.append(temp)
                    upper_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['shift_down'])
                    temp = keyboard_dict[temp]['shift_down']

# TODO:: Left and Right Parsing
    elif direction == 'RIGHT':
        left_char = find_end_keys(direction,initial_character)
        for i in range(1,n):
            if str(initial_character).islower() or str(initial_character).isalnum() or str(initial_character) in ['[',']','\\',';',"'",',','.','/','-','=']:
                if keyboard_dict[temp]['right'] == left_char:
                    temp = keyboard_dict[left_char]['down']
                    parse_stack.append(temp)
                    left_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['right'])
                    temp = keyboard_dict[temp]['right']
            else:
                if keyboard_dict[temp]['shift_right'] == left_char:
                    temp = keyboard_dict[left_char]['shift_down']
                    parse_stack.append(temp)
                    left_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['shift_right'])
                    temp = keyboard_dict[temp]['shift_right']
    
    elif direction == 'LEFT':
        right_char = find_end_keys(direction,initial_character)
        for i in range(1,n):
            if str(initial_character).islower() or str(initial_character).isalnum() or str(initial_character) in ['[',']','\\',';',"'",',','.','/','-','=']:
                if keyboard_dict[temp]['left'] == right_char:
                    temp = keyboard_dict[right_char]['down']
                    parse_stack.append(temp)
                    right_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['left'])
                    temp = keyboard_dict[temp]['left']
            else:
                if keyboard_dict[temp]['shift_left'] == right_char:
                    temp = keyboard_dict[right_char]['shift_down']
                    parse_stack.append(temp)
                    right_char = temp
                else:
                    parse_stack.append(keyboard_dict[temp]['shift_left'])
                    temp = keyboard_dict[temp]['shift_left']

def skip_and_parse(skip_val,start_char):
    global parse_stack
    pattern_stack = []
    start_index = 0
    for i in range(0,len(parse_stack)):
        if parse_stack[i] == str(start_char):
            start_index = i
            break

    for i in range(start_index,len(parse_stack),int(skip_val)):
        pattern_stack.append(parse_stack[i])
    
    return pattern_stack


if __name__ == '__main__':
    load_keyboard_data()
    generate_keyboard_patters('1','RIGHT',46)
    print(parse_stack)

    for i in range(1,11):
        for j in ['a']:
            temp_dict = {}
            temp_dict[i] = skip_and_parse(i,j)
            # print(temp_dict)
            possible_patterns_data_set[str(i)+j] = temp_dict
    
    pprint(possible_patterns_data_set)
    # temp_list = possible_patterns_data_set['4a'][4]
    # print(temp_list)
    # find_combinations(temp_list)

    print("Combinations")
    print(possible_password_list)
    # find_interstion_with_data()
    # print("After finding intersection")
    # print(matched_passwords)
    # poss_list = []
    # limit = 1
    # while True:
    #     str1 = ''
    #     for i in range(0,len(temp_list),limit):
    #         str1 += temp_list[i]
    #         poss_list.append(str1)
        
    #     limit += 1
    #     if limit == 3:
    #         break
    
    # print(poss_list)
        



# For all letter width from 3-15, in down direction and up direction
# Formatting of the leaked password
# Intersection of the leaked password
# Skipping Letters from the list