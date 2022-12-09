"""
This python module finds the intersection with the datasets provided
Required Datasets: Passwords - a text data path and the generated data to match
"""


matched_passwords = []
pwd_gen_arr = []

def send_pwd_to_arr(gen_pwd_path):
    global pwd_gen_arr
    file2 = open(gen_pwd_path,'rb')
    for j in file2:
        j = str(j).replace("b'",'').replace("\\n'",'')
        pwd_gen_arr.append(j)

def find_interstion_with_data(pwd_db_path):
    global matched_passwords
    global pwd_gen_arr
    file = open(pwd_db_path,'rb')
    
    for i in file:
        i = str(i).replace("b'",'').replace("\\n'",'')
        if i in pwd_gen_arr:
            print("Match found",i)
            matched_passwords.append(i)


if __name__ == "__main__":
    # parse_the_graph(adjancency_graph,'a',3)
    pwd_db_path = "passwords.txt"
    gen_pwds = "generated/three_letter_combinations.txt"
    send_pwd_to_arr(gen_pwds)
    find_interstion_with_data(pwd_db_path)
    print(len(matched_passwords))