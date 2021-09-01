import os
import string
import random
import time
from tabulate import tabulate

def viewPassword():
    file_path = 'passwords.txt'
    if os.stat(file_path).st_size == 0:
        print(bcolors.WARNING+"\n["+bcolors.OKRED+"!"+bcolors.WARNING+"]"+ bcolors.OKRED+"  N.A"+bcolors.ENDC)
    else:
        myFile = open("passwords.txt", "r")
        print("\n")
        print(bcolors.OKGREEN+myFile.read()+bcolors.ENDC)
        print("\n")
        myFile.close()


def savePassword(tmp):
    acc = input(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"-"+bcolors.OKBLUE+"]"+ bcolors.WARNING +"  This password is for: "+bcolors.ENDC)

    myFile = open("passwords.txt", "a")
    myFile.write("\n"+tabulate([[tmp, acc]], headers=['Passwords', 'Account'], tablefmt='grid')+"\n")
    myFile.close()

    print(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"+"+bcolors.OKBLUE+"]"+ bcolors.OKGREEN +"  Password saved at passwordAnalyzer/passwords.txt\n"+bcolors.ENDC)


def createPassword():
    str1 = string.ascii_lowercase
    str2 = string.ascii_uppercase
    str3 = string.digits
    str4 = string.punctuation

    while True:
        passwordLength = int(input(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"-"+bcolors.OKBLUE+"]"+ bcolors.WARNING+"  Enter the password length(>8): "+bcolors.ENDC))
        try:
            if(passwordLength >8):
                break
            else:
                raise RuntimeError
        except RuntimeError :
            print(bcolors.WARNING+"\n["+bcolors.OKRED+"!"+bcolors.WARNING+"]"+ bcolors.OKRED+"  Password Length should be more than 8. Please try again...\n"+bcolors.ENDC)

    str = []
    str.extend(list(str1))
    str.extend(list(str2))
    str.extend(list(str3))
    str.extend(list(str4))

    random.shuffle(str)

    tmp = ''.join(str[0:passwordLength])
    print(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"+"+bcolors.OKBLUE+"]"+ bcolors.WARNING+"  Your password is: " + bcolors.OKMAGANTA + tmp + bcolors.ENDC)

    while True:
        choice2 = input(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"-"+bcolors.OKBLUE+"]"+ bcolors.WARNING +"  Do you want us to save your password or not? (Y/N) : "+bcolors.ENDC)
        try:
            if(choice2 == 'Y' or choice2 =='y'):
                savePassword(tmp)
                break
            elif(choice2 == 'N' or choice2 == 'n'):
                mainMenu()
                break
            else:
                raise RuntimeError
        except RuntimeError:
            print(bcolors.WARNING+"\n["+bcolors.OKRED+"!"+bcolors.WARNING+"]"+ bcolors.OKRED+"  Oops! That's not the valid input. Please try again...\n"+bcolors.ENDC)
      

def analyzePassword():
    password = input(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"-"+bcolors.OKBLUE+"]"+ bcolors.WARNING+"  Enter your password: "+bcolors.ENDC)
    passwordAsList = list(password)
    length = len(password)
    upper = lower = numerical =  alnum = 0

    for x in passwordAsList:
        if(x.isupper() == 1):
            upper = 1
        if(x.islower() == 1):
            lower = 1
        if(x.isnumeric() == 1):
            numerical = 1
        if(x.isalnum() == 0):
            alnum = 1

    if(upper == 0):
        print(bcolors.OKYELLOW+"\n["+bcolors.OKRED+"!"+bcolors.OKYELLOW+"]"+ bcolors.OKGREEN +"  Uppercase letters missing."+bcolors.ENDC)
        time.sleep(1)
    if(lower == 0):
        print(bcolors.OKYELLOW+"["+bcolors.OKRED+"!"+bcolors.OKYELLOW+"]"+ bcolors.OKGREEN +"  Lowercase letters missing."+bcolors.ENDC)
        time.sleep(1)
    if(numerical == 0):
        print(bcolors.OKYELLOW+"["+bcolors.OKRED+"!"+bcolors.OKYELLOW+"]"+ bcolors.OKGREEN +"  Numbers missing."+bcolors.ENDC)
        time.sleep(1)
    if(alnum == 0):
        print(bcolors.OKYELLOW+"["+bcolors.OKRED+"!"+bcolors.OKYELLOW+"]"+ bcolors.OKGREEN +"  Special Characters missing."+bcolors.ENDC)
        time.sleep(1)
    if(length <= 8 ):
        print(bcolors.OKYELLOW+"["+bcolors.OKRED+"!"+bcolors.OKYELLOW+"]"+ bcolors.OKGREEN +"  Unsatisfying password length."+bcolors.ENDC)
        time.sleep(1)
    if(upper == 1 and lower == 1 and numerical == 1 and alnum == 1 and length > 8):
        print("N.A")

    if(upper == 0 or lower == 0 or numerical == 0 or alnum == 0):
        print(bcolors.OKYELLOW+"\n["+bcolors.OKRED+"!"+bcolors.OKYELLOW+"]"+ bcolors.OKRED +"  Make your password stronger."+bcolors.ENDC)
        while True:
            choice1 = str(input(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"-"+bcolors.OKBLUE+"]"+ bcolors.WARNING +"  Want us to suggest a password for you? (Y/N) : "+bcolors.ENDC))
            try:
                if(choice1 == 'Y' or choice1 == 'y'):
                    createPassword()
                    break
                elif(choice1 == 'N' or choice1 == 'n'):
                    mainMenu()
                    break
                else:
                    raise RuntimeError
            except RuntimeError:
                print(bcolors.WARNING+"\n["+bcolors.OKRED+"!"+bcolors.WARNING+"]"+ bcolors.OKRED+"  Oops! That's not the valid input. Please try again...\n"+bcolors.ENDC)

class bcolors:
    HEADER = '\033[95;1m'
    OKBLUE = '\033[94;1m'
    OKCYAN = '\033[96;1m'
    OKGREEN = '\033[92;1m'
    OKRED = '\u001b[31;1m'
    OKYELLOW = '\u001b[33;1m'
    OKMAGANTA = '\u001b[35;1m'
    WARNING = '\033[93;1m'
    FAIL = '\033[91;1m'
    ENDC = '\033[0;1m'
    BOLD = '\033[1;1m'
    UNDERLINE = '\033[4;1m'

heading = """
'########::'##:::::::::'######:::'######::'##:::::'##:::'#####:::'########::'########::::::::::::::'###::::'##::: ##:'##::::::::'##:::::::'##:::'##:'########::'#######::'########::
 ##.... ##: ##:::'##::'##... ##:'##... ##: ##:'##: ##::'##.. ##:: ##.... ##: ##.... ##::::::::::::'## ##::: ###:: ##: ##:::'##:: ##:::::::. ##:'##::..... ##::'##.... ##: ##.... ##:
 ##:::: ##: ##::: ##:: ##:::..:: ##:::..:: ##: ##: ##:'##:::: ##: ##:::: ##: ##:::: ##:::::::::::'##:. ##:: ####: ##: ##::: ##:: ##::::::::. ####::::::: ##:::..::::: ##: ##:::: ##:
 ########:: ##::: ##::. ######::. ######:: ##: ##: ##: ##:::: ##: ########:: ##:::: ##:'#######:'##:::. ##: ## ## ##: ##::: ##:: ##:::::::::. ##::::::: ##:::::'#######:: ########::
 ##.....::: #########::..... ##::..... ##: ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##:........: #########: ##. ####: #########: ##:::::::::: ##:::::: ##::::::...... ##: ##.. ##:::
 ##::::::::...... ##::'##::: ##:'##::: ##: ##: ##: ##:. ##:: ##:: ##::. ##:: ##:::: ##:::::::::: ##.... ##: ##:. ###:...... ##:: ##:::::::::: ##::::: ##::::::'##:::: ##: ##::. ##::
 ##:::::::::::::: ##::. ######::. ######::. ###. ###:::. #####::: ##:::. ##: ########::::::::::: ##:::: ##: ##::. ##::::::: ##:: ########:::: ##:::: ########:. #######:: ##:::. ##:
..:::::::::::::::..::::......::::......::::...::...:::::.....::::..:::::..::........::::::::::::..:::::..::..::::..::::::::..:::........:::::..:::::........:::.......:::..:::::..::

"""
print(bcolors.OKMAGANTA+heading)
print(bcolors.OKYELLOW+".:.:."+bcolors.ENDC+" Password Manager coded by: @Himmii "+bcolors.OKYELLOW+".:.:.")

def mainMenu():
    while True:
        try:
            print(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"1"+bcolors.OKBLUE+"]"+ bcolors.WARNING +"  Analyze Your Password. \n" + bcolors.OKBLUE+"["+bcolors.OKGREEN+"2"+bcolors.OKBLUE+"]"+bcolors.WARNING+"  Create Your Password."+bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"3"+bcolors.OKBLUE+"]"+ bcolors.WARNING+"  Save Your Password."+bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"4"+bcolors.OKBLUE+"]"+ bcolors.WARNING +"  View Saved Passwords. " +bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"5"+bcolors.OKBLUE+"]"+ bcolors.WARNING +"  Quit. \n")
            choice = int(input(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"-"+bcolors.OKBLUE+"]"+ bcolors.WARNING+"  Enter your choice: "+bcolors.ENDC))
            if(choice == 1):
                analyzePassword()
            elif(choice == 2):
                createPassword()
            elif(choice == 3):
                tmp = input(bcolors.OKBLUE+"\n["+bcolors.OKGREEN+"-"+bcolors.OKBLUE+"]"+ bcolors.WARNING +"  Enter your password to be saved: "+bcolors.ENDC)
                savePassword(tmp)
            elif(choice == 4):
                viewPassword()
            elif(choice == 5):
                break
            else:
                raise RuntimeError
        
        except (ValueError,RuntimeError):
            print(bcolors.WARNING+"\n["+bcolors.OKRED+"!"+bcolors.WARNING+"]"+ bcolors.OKRED+"  Oops! That's not the valid input. Please try again...\n"+bcolors.ENDC)

mainMenu()