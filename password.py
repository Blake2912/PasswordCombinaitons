import sys
from pprint import pprint
possible_password_list = []
matched_passwords = []

def find_combinations(ip_list):
    for i in range(3,16):
        for j in range(0,3):
            parse_list(ip_list,i,j)

def find_interstion_with_data():
    """
    This function requires the path of the passwords database for matching...
    """
    global possible_password_list
    global matched_passwords
    password_db_path = input("\nEnter the path where the password db txt file path:").strip()
    try:
        file = open(password_db_path,'rb')
        print("\nThis will take couple of minutes to finish please wait...\n")
        for i in file:
            i = str(i).replace("b'",'').replace("\\n'",'')
            if i in possible_password_list:
                print("Match found",i)
                matched_passwords.append(i)
    except:
        print("Please enter the path of the password database properly \
            \nfile not found")


def parse_list(ip_list,no_of_chars,skip_chars,file_name):
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
                    possible_password_list.append(res_str)
                    file_name.write(res_str+"\n")
                
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
            possible_password_list.append(res_str)
            file_name.write(res_str+"\n")


# Checking for only four args
if len(sys.argv) != 4:
    print("Invalid arguments passed please re-run the program with four arguments only!")
    print("Follow this format: python3 password.py <direction> <no of characters> <skip characters>")
    print("The direction can be h -> horizontal h_s -> horizontal shift v -> vertical and v_s -> vertical shift")
    exit(0)
else:
    # Checking for proper command line params
    if sys.argv[1].lower() in ['h','h_s','v','v_s'] and sys.argv[2].isdigit() and sys.argv[3].isdigit():
        direction = sys.argv[1].lower()
        no_of_chars = int(sys.argv[2])
        skip_chars = int(sys.argv[3])
    else:
        print("Follow this format: python3 password.py <direction> <no of characters> <skip characters>")
        print("The direction can be h -> horizontal h_s -> horizontal shift v -> vertical and v_s -> vertical shift")
        exit(0)


    if direction == 'h':
        # Horizontal parsing
        horizontal_list = ['`','1','2','3','4','5','6','7','8','9','0','-','=','q',
        'w','e','r','t','y','u','i','o','p','[',']','\\','a','s','d','f','g','h','j',
        'k','l',';',"'",'z','x','c','v','b','n','m',',','.','/']
        file = open("horizontal.txt","w")
        parse_list(horizontal_list,no_of_chars,skip_chars,file)
        # find_combinations(horizontal_list)
        pprint(possible_password_list)
        print("Count: ",len(possible_password_list))

    elif direction == 'h_s':
        # Horizontal-Shift parsing
        horizontal_shift_list = ['~','!','@','#','$','%','^','&','*','(',')','_',
        '+','Q','W','E','R','T','Y','U','I','O','P','{','}','|','A','S','D','F','G',
        'H','J','K','L',':','"','Z','X','C','V','B','N','M','<','>','?']
        file = open("horizontal_shift.txt","w")
        parse_list(horizontal_shift_list,no_of_chars,skip_chars,file)
        pprint(possible_password_list)
        print("Count: ",len(possible_password_list))


    elif direction == 'v':
        # Vertical parsing
        vertical_list = ['`','1','q','a','z','2','w','s','x','3','e','d','c','4','r','f',
        'v','5','t','g','b','6','y','h','n','7','u','j','m','8','i','k',',','9','o','l','.','0','p',
        ';','/','-','[',"'",'=',']','\\']
        file = open("vertical.txt","w")
        parse_list(vertical_list,no_of_chars,skip_chars,file)
        # find_combinations(vertical_list)
        pprint(possible_password_list)
        print("Count: ",len(possible_password_list))


    elif direction == 'v_s':
        # Vertical-shift parsing
        vertical_shift_list = ['~','!','Q','A','Z','@','W','S','X','#','E','D','C','$','R','F','V',
        '%','T','G','B','^','Y','H','N','&','U','J','M','*','I','K','<','(','O','L','>',')','P',':',
        '?','_','{','"','+','}','|']
        file = open("vertical_shift.txt","w")
        parse_list(vertical_shift_list,no_of_chars,skip_chars,file)
        pprint(possible_password_list)
        print("Count: ",len(possible_password_list))

print("Possible passwords collected!")
ack_find_match = input("\nPlease type yes, \
    \nif you want the passwords to be matched with the dataset: ")
if str(ack_find_match).lower() == 'yes':
    # Find the match
    find_interstion_with_data()
    print("Matched passwords")
    print(matched_passwords)
    print("No of matched password combination",len(matched_passwords))
