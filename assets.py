from pytube import *
from colorama import *
import pyfiglet

def spaces():
    print("")
    print("")
    print("")

def title():
    title_txt = pyfiglet.figlet_format("Y O U T U B E", "bloody")
    print(Fore.YELLOW + title_txt)

def menuItems():
    print(Fore.GREEN + " [1] Downloader ")
    print(Style.RESET_ALL)
    print(Fore.RED + " [2] Exit ")
    print(Style.RESET_ALL)

def mainMenu():
    spaces()
    title()
    spaces()
    menuItems()
    print("")

def downloadVideo():
    print(Fore.BLUE + "====== Enter YouTube Link")
    print("||")
    link = input("===> ")
    print(Style.RESET_ALL)
    print("")
    data = YouTube(link)
    video = data.streams.all()
    vid = list(enumerate(video))
    for i in vid:
        print(i)
        print("")
    print("")
    print(Fore.BLUE + "====== Enter You Like As YouTube Video Number")
    print("||")
    chooseVid = int(input("===> "))
    print(Style.RESET_ALL)
    print("")
    print(Fore.MAGENTA + "Downloading ...............")
    print(Style.RESET_ALL)
    print("")
    video[chooseVid].download()
    print(Back.GREEN + "Dowloading Succesfull")
    print(Style.RESET_ALL)
    spaces()
    exit()

'''
def colorsGet():
    x = 0
    for rows in range(24):
        colors = ""
        for columns in range(5):
            code = str(x + columns)
            colors = colors + "\033[" + code + "m\\33[" + code + "m\033[0m" + " "
            print(colors)
            x += 5
'''
