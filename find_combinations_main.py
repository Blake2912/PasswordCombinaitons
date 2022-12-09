# The integrated code for finding all combinations will be done
from os import mkdir
import json
from pprint import pprint


FREQUENCY_DICT = {}
COMBINATIONS = []
MAXIMUM_CHARS = 7
KEYBOARD_DATA = {}

def load_keyboard_data():
    keyboard_json = open('adjacency.json')
    temp = json.load(keyboard_json)
    print("Initialized the keyboard data!")
    return temp


def seven_letter_combination(graph,ip_char,folder_name):
    try:
        txt_file = open("{0}/7_letter_combinations.txt".format(folder_name),'a')
    except:
        mkdir(folder_name)
        txt_file = open("{0}/7_letter_combinations.txt".format(folder_name),'a')
    for a in graph[ip_char]:
        for b in graph[a]:
            for c in graph[b]:
                for d in graph[c]:
                    for e in graph[d]:
                        for f in graph[e]:
                            temp_str = ip_char + a + b + c + d + e + f
                            txt_file.write(temp_str+"\n")


def eight_letter_combinations(graph,ip_char,folder_name):
    try:
        txt_file = open("{0}/eight_letter_combinations.txt".format(folder_name),'a')
    except:
        mkdir(folder_name)
        txt_file = open("{0}/eight_letter_combinations.txt".format(folder_name),'a')
    for a in graph[ip_char]:
        for b in graph[a]:
            for c in graph[b]:
                for d in graph[c]:
                    for e in graph[d]:
                        for f in graph[e]:
                            for g in graph[f]:
                                temp_str = ip_char + a + b + c + d+ e + f + g
                                txt_file.write(temp_str+"\n")
    print("Generated/8_combinations.txt!")


def open_main_file(pwd_path,no_of_chars,folder_name):
    global MAXIMUM_CHARS
    try:
        txt_file = open("Combinations starting with {0}/{1}_letter_combinations.txt".format(folder_name,MAXIMUM_CHARS-no_of_chars),'w')
    except:
        mkdir(folder_name)
        txt_file = open("Combinations starting with {0}/{1}_letter_combinations.txt".format(folder_name,MAXIMUM_CHARS-no_of_chars),'w')
    # file = open(pwd_path,'rb')
    
    with open(pwd_path,'r+') as f:
        lines = f.readlines()
        for i in lines:
            i = i[:len(i)-(no_of_chars)-1]
            txt_file.write(i+"\n")
        f.close()
        txt_file.close()


def check_for_duplicates(pwd_path,no_of_chars):
    print("Checking for duplicates at",pwd_path)
    with open(pwd_path,'r+') as fp:
        lines = fp.readlines()
        tmp_dict = {}
        for i in lines:
            tmp = i.replace("\n","")
            if tmp in tmp_dict:
                tmp_dict[tmp] += 1
            else:
                tmp_dict[tmp] = 0
        
        fp.close()
    with open(pwd_path,'w') as gen_file:
        gen_file.truncate()
        dict_keys = list(tmp_dict.keys())
        for i in dict_keys:
            if len(i) == no_of_chars:
                gen_file.write(i + "\n")
        gen_file.close()
    print("Duplicate check complete")


def find_number_of_lines(pwd_path):
    with open(pwd_path,'r+') as fp:
        print("No of lines in the files: {0}".format(len(fp.readlines())))


if __name__ == "__main__":
    adjancency_graph = load_keyboard_data()

    with open("keyboard.txt",'r+') as keyboard:
        for i in keyboard.readlines():
            lis = list(i)
            try:
                lis.remove("\n")
            except:
                print("No new line present in lis")
            KEYBOARD_DATA["".join(lis)] = lis

    for i in KEYBOARD_DATA.keys():
        for j in KEYBOARD_DATA[i]:
            seven_letter_combination(adjancency_graph,j,"Combinations starting with {0}".format(i))
        
        print("Generated Combinations starting with {0}/7_combinations.txt!".format(i))
        check_for_duplicates("Combinations starting with {0}/7_letter_combinations.txt".format(i),MAXIMUM_CHARS)

        for x in range(1,5):
            open_main_file("Combinations starting with {0}/7_letter_combinations.txt".format(i),x,i)
            check_for_duplicates("Combinations starting with {0}/{1}_letter_combinations.txt".format(i,MAXIMUM_CHARS-x),MAXIMUM_CHARS-x)

    # printable_chars_arr = ["q","w","e","r","t","y","u","i","o","p","[","]","\\"]

    # for i in printable_chars_arr:
    #     seven_letter_combination(adjancency_graph,i)
    
    # print("Generated/7_combinations.txt!")
    # check_for_duplicates("generated/7_letter_combinations.txt",MAXIMUM_CHARS)
    
    # for i in range(1,5):
    #     open_main_file("generated/7_letter_combinations.txt",i)
    #     check_for_duplicates("generated/{0}_letter_combinations.txt".format(MAXIMUM_CHARS-i),MAXIMUM_CHARS-i)


