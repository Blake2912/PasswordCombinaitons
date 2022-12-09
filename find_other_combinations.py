from os import mkdir
from pprint import pprint
import pwd
import json

def open_main_file(pwd_path,no_of_chars):
    try:
        txt_file = open("generated/{0}_letter_combinations.txt".format(7-no_of_chars),'w')
    except:
        mkdir("generated")
        txt_file = open("generated/{0}_letter_combinations.txt".format(7-no_of_chars),'w')
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


# find_number_of_lines("generated/eight_letter_combinations.txt")

for i in range(1,5):
    open_main_file("generated/7_letter_combinations.txt",i)
    check_for_duplicates("generated/{0}_letter_combinations.txt".format(7-i),7-i)
# check_for_duplicates("generated/7_letter_combinations.txt",7)

# open_main_file("generated/eight_letter_combinations.txt",1)
# check_for_duplicates("generated/7_letter_combinations.txt")