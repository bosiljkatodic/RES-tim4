import socket
from unicodedata import name

MENU_PROMPT = """
CHOOSE OPTION:

1) ANALOGNO 
2) DIGITALNO

Your selection: 
"""

MENU_PROMPT2 = """
CHOOSE OPTION:

1) ON 
2) OFF

Your selection: 
"""

MENU_PROMPT3 = """
CHOOSE OPTION:

1) Unesite pocetnu vrednost:

"""

if __name__ == "__main__":
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(),4000))
    #msg=s.recv(1024)

    state=""
    actual_value=""

    user_input = input(MENU_PROMPT)
    if user_input == "1":
        state="ANALOGNO"
        actual_value=input(MENU_PROMPT3)

    elif user_input == "2":
        state="DIGITALNO"
        user_input2 = input(MENU_PROMPT2)
        if user_input2 == "1":
            actual_value="ON"
        elif user_input2 == "2":
            actual_value="OFF"
        else:
            print("Invalid input, please try again!")

    else:
        print("Invalid input, please try again!")



