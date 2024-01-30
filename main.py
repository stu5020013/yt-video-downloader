from assets import *
from colorama import *

mainMenu()

print(Fore.BLUE + "====== Enter Number")
print("||")
chooseNum = int(input("===> "))
print(Style.RESET_ALL)

print("")

if chooseNum == 1:
    downloadVideo()
elif chooseNum == 2:
    print(Fore.RED + "Exiting ...............")
    print(Style.RESET_ALL)
    spaces()
    exit()
else:
    print(Fore.RED + "Error ...............")
    print(Style.RESET_ALL)
    spaces()
    exit()

spaces()
