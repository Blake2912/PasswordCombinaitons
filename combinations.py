import json
from lib2to3.pgen2 import driver
from os import mkdir
from pprint import pprint


FREQUENCY_DICT = {}
COMBINATIONS = []

def load_keyboard_data():
    keyboard_json = open('adjacency.json')
    temp = json.load(keyboard_json)
    print("Initialized the keyboard data!")
    return temp

def four_letter_combinations(graph,input_arr):
    try:
        txt_file = open("generated/four_letter_combinations.txt",'w')
    except:
        mkdir("generated")
        txt_file = open("generated/four_letter_combinations.txt",'w')
    for i in input_arr:
        for j in graph[i]:
            for k in graph[j]:
                for l in graph[k]:
                    temp_str = i + j + k + l
                    txt_file.write(temp_str+"\n")
    print("Check generated/four_letter_combinations.txt!")

def three_letter_combinations(graph,input_arr):
    try:
        txt_file = open("generated/three_letter_combinations.txt",'w')
    except:
        mkdir("generated")
        txt_file = open("generated/three_letter_combinations.txt",'w')
    for i in input_arr:
        for j in graph[i]:
            for k in graph[j]:
                    temp_str = i + j + k
                    txt_file.write(temp_str+"\n")
                    # COMBINATIONS.append(temp_str)
    print("Check generated/three_letter_combinations.txt!")

def five_letter_combinations(graph,input_arr):
    try:
        txt_file = open("generated/five_letter_combinations.txt",'w')
    except:
        mkdir("generated")
        txt_file = open("generated/five_letter_combinations.txt",'w')
    for i in input_arr:
        for j in graph[i]:
            for k in graph[j]:
                for l in graph[k]:
                    for m in graph[l]:
                        temp_str = i + j + k + l + m
                        txt_file.write(temp_str+"\n")
    print("Check generated/five_letter_combinations.txt!")


# Functions to find the intersection of passwords and then store it in a JSON file for further analysis

pwd_gen_arr = []

def send_pwd_to_arr(gen_pwd_path):
    global pwd_gen_arr
    pwd_gen_arr = []
    file2 = open(gen_pwd_path,'rb')
    for j in file2:
        j = str(j).replace("b'",'').replace("\\n'",'')
        pwd_gen_arr.append(j)

def find_interstion_with_data(pwd_db_path):
    matched_passwords = []
    global pwd_gen_arr
    global COMBINATIONS
    file = open(pwd_db_path,'rb')
    
    for i in file:
        i = str(i).replace("b'",'').replace("\\n'",'')
        if i in pwd_gen_arr:
            print("Match found",i)
            matched_passwords.append(i)
    return len(matched_passwords)

def seven_letter_combination(graph,ip_char):
    """
    Modification: The function is now modified to get only the input character instead of an input array
    for faster intersection results.
    """
    try:
        txt_file = open("generated/7_letter_combinations.txt",'a')
    except:
        mkdir("generated")
        txt_file = open("generated/7_letter_combinations.txt",'a')

    for a in graph[ip_char]:
        for b in graph[a]:
            for c in graph[b]:
                for d in graph[c]:
                    for e in graph[d]:
                        for f in graph[e]:
                            temp_str = ip_char + a + b + c + d + e + f
                            txt_file.write(temp_str+"\n")
    print("Generated/seven_letter_combinations.txt!")

def eight_letter_combinations(graph,ip_char):
    try:
        txt_file = open("generated/eight_letter_combinations.txt",'a')
    except:
        mkdir("generated")
        txt_file = open("generated/eight_letter_combinations.txt",'a')
    for a in graph[ip_char]:
        for b in graph[a]:
            for c in graph[b]:
                for d in graph[c]:
                    for e in graph[d]:
                        for f in graph[e]:
                            for g in graph[f]:
                                temp_str = ip_char + a + b + c + d+ e + f + g
                                txt_file.write(temp_str+"\n")

def driver_function(graph,input_arr):
    pwd_db_path = "passwords.txt"
    gen_pwds = "generated/seven_letter_combinations.txt"
    for i in input_arr:
        seven_letter_combination(graph,i)
        # send_pwd_to_arr(gen_pwds)
        # FREQUENCY_DICT[i] = find_interstion_with_data(pwd_db_path)

    

if __name__ == "__main__":
    adjancency_graph = load_keyboard_data()
    # printable_chars_arr = list(adjancency_graph.keys())
    printable_chars_arr = ["1","2","3","4","5","6","7","8","9","0","-","+"]
    driver_function(adjancency_graph,printable_chars_arr)

    