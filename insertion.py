#========== Modules ========== 
from os import system,path
from string import ascii_uppercase as uppercase
from string import ascii_lowercase as lowercase
from Paranoia_lib.colorama import init
from Paranoia_lib.colorama import Fore,Back,Style
init()
from Paranoia_lib.pwinput import pwinput
from secrets import choice
#========== End of Modules ========== 
#========== Global Vars ========== 
fullchar=uppercase+lowercase + '!@#$%^&*()?'+r'{}'+'-+=_|<>,.[]~`"0123456789 '
numbers=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88','89','90']
#========== End of Global Vars ========== 

print(Style.BRIGHT+Fore.RED+"""
================================================================================================================================================================
 _______                                                   __        __        ______                                           __      __                     
|       \                                                 |  \      |  \      |      \                                         |  \    |  \                    
| ???????\ ______    ______   ______   _______    ______   \??  ____| ??       \?????? _______    _______   ______    ______  _| ??_    \??  ______   _______  
| ??__/ ??|      \  /      \ |      \ |       \  /      \ |  \ /      ??        | ??  |       \  /       \ /      \  /      \|   ?? \  |  \ /      \ |       \ 
| ??    ?? \??????\|  ??????\ \??????\| ???????\|  ??????\| ??| ????????        | ??  | ???????\|  ???????|  ??????\|  ??????\\??????   | ??|  ??????\| ???????\\
| ??????? /      ??| ??   \??/      ??| ??  | ??| ??  | ??| ??| ??  | ??        | ??  | ??  | ?? \??    \ | ??    ??| ??   \?? | ?? __ | ??| ??  | ??| ??  | ??
| ??     |  ???????| ??     |  ????????|??  | ??| ??__/ ??| ??| ??__| ??       _| ??_ | ??  | ?? _\??????\| ?????????|??       | ??|  \| ??| ??__/ ??| ??  | ??
| ??      \??    ??| ??      \??    ??| ??  | ?? \??    ??| ?? \??    ??      |   ?? \| ??  | ??|       ?? \??     \| ??        \??  ??| ?? \??    ??| ??  | ??
 \??       \??????? \??       \??????? \??   \??  \??????  \??  \???????       \?????? \??   \?? \???????   \??????? \??         \????  \??  \??????  \??   \??

================================================================================================================================================================                                                                                                                                                             
                                                                                                                                                               
                                                                                                                                                               
"""+Fore.WHITE)

                                                                                                                             
                                                                                                                                                               

print(Style.BRIGHT+"Hello, welcome to the"+Fore.RED+" Paranoid plaintext insertion "+Fore.WHITE)
print("Why paranoid? Because it helps keeping the insertion hidden\nfrom both"+" keyloggers "+Fore.WHITE+"and for the chance of someone"+Fore.RED+" monitoring "+Fore.WHITE+"your system.")
print('The only "cost" this method has is that its slow, because you gotta insert the characters one by one\n')
print(Back.RED+'INSTRUCTIONS'+Back.RESET+':')
print('For a every character you are gonna enter there is gonna be a table\nwith numbers in '+Fore.RED+"red"+Fore.WHITE+" and the characters.\nBased on the character you want, you will choose the number in "+Fore.RED+"red"+Fore.WHITE+" pointing at it.\nEvery time you enter a character the table will change,\nThe row of characters will stay the same(uppercase,lowercase,symbols,numbers and space),\nbut the "+Fore.RED+"red"+Fore.WHITE+" numbers will be shuffled.\n\nWhen you are done simply dont insert anything and just press enter")
print("As instructions said inserting nothing will end the program, dont worry though there will be a verification so if you enter nothing by accident you can go back")

def randchoice(fullchar,numbers):
    phrase=""
    tempchars=[]
    print(Style.BRIGHT+Fore.RED+"=================================================================================================="+Fore.WHITE)
    for count1 in range(len(numbers)):
        tempnum=choice(numbers)
        while tempnum in tempchars:
            tempnum=choice(numbers)
        tempchars.append(tempnum)
    dicti0nary={}
    for count2 in range(len(numbers)):
        dicti0nary.update({tempchars[count2]: fullchar[count2] })
    item=""
    count=0
    for key, value in dicti0nary.items():
        item+=f"{Fore.LIGHTRED_EX}{key}{Fore.WHITE} --> {value}  " 
        count+=1
        if count==10:
            count=0
            print(item)
            item=""   
    print(Fore.RED+"=================================================================================================="+Fore.WHITE)
    print("")
    option=pwinput(prompt="Input the character you want"+Fore.RED+" --> ",mask="?")
    while option not in numbers:
        if option=="":
            print('')
            print(Back.RED+Fore.WHITE+"WARNING!!!"+Back.RESET,"By exiting you stop the insertion.\nFor obvious reasons(this method is reallyyy slow)...Are you sure you want to stop?")
            exitoption=input(Fore.GREEN+"Y"+Fore.WHITE+'/'+Fore.RED+"N"+Fore.WHITE+" --> ")
            while exitoption!="y" and exitoption!="Y" and exitoption!="N" and exitoption!="n":
                print(exitoption)
                exitoption=input(Fore.RED+"Uh oh Error "+Fore.WHITE+"The input must be either a "+Fore.GREEN+"Y"+Fore.WHITE+" or a "+Fore.RED+"N --> ")
            
            if exitoption=="Y" or exitoption=="y":
                return False
            else:
                print("Back to writing..")
                option=pwinput(prompt=Fore.RED+"Uh oh Error "+Fore.WHITE+"The input must be one of the"+Fore.RED+" red "+Fore.WHITE+"numbers.\nInput the character you want"+Fore.RED+" --> ",mask="?")
        else:
            option=pwinput(prompt=Fore.RED+"Uh oh Error "+Fore.WHITE+"The input must be one of the"+Fore.RED+" red "+Fore.WHITE+"numbers.\nInput the character you want"+Fore.RED+" --> ",mask="?")
    
    phrase+=dicti0nary[option]
    return phrase
while True:
    plaintext=""
    phrase=randchoice(fullchar,numbers)
    while phrase!=False:
        plaintext+=phrase+""
        phrase=randchoice(fullchar,numbers)
    print("Wanna print what you inserted or save it in a file\n")
    print("1. Print that shite")
    print("2. Save that shite\n\n")
    ui=input("-->")
    while ui != "1" and ui != "2":
        print(Fore.RED+"Uh oh Error "+Fore.WHITE+"The input must be either '1' or '2'")
        ui=input("-->")
    match ui:
        case "1":
            print(plaintext)
        case "2":
            print("File name? (no need to write an ext its gonna be a txt) ")
            filename=input("-->")
            with open(f"{filename}.txt", "a") as file:
                file.writelines(plaintext)
    print("Wanna kill me :(")  
    kill=input(Fore.GREEN+"Y"+Fore.WHITE+'/'+Fore.RED+"N"+Fore.WHITE+" --> ")
    while kill.lower()!="y" and kill.lower()!="n":
            exitoption=input(Fore.RED+"Uh oh Error "+Fore.WHITE+"The input must be either a "+Fore.GREEN+"Y"+Fore.WHITE+" or a "+Fore.RED+"N --> ")    
    if kill.lower() == 'y':
           break;