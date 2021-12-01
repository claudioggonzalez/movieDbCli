#!/bin/python3

from typing import Optional
from simple_term_menu import TerminalMenu
import configparser
import json
import requests

DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3
CRITICAL = 4

def printLog(msgLogLevel, logMessage):
    if msgLogLevel >= LOG_LEVEL:
        print(logMessage)

def getMovieById():
    options = ["[1]Define ID to get","[0]Return MAIN MENU"]
    menuEntryIdx = displayMenu(options, "GET MOVIE BY ID:\n-----------------")
    
    if options[menuEntryIdx] == options[0]:
        id = int(input("Movie ID: "))
        requests
    elif options[menuEntryIdx] == options[1]:
        main()
    else:
        print("Opción Desconocida!!!")
        exit(1)

def displayMenu(options, menuTitle):
    menu = TerminalMenu(options, title=menuTitle)
    idx = menu.show()
    return idx

def main():
    options = ["[1]Get Movie by ID","[2]Get Movie by Title","[3]Get Batch of Movies","[4]Add Movie","[5]Update Movie Data","[6]Delete Movie", "[7]API Info", "[0]Exit"]
    menuEntryIdx = displayMenu(options, "MAIN MENU:\n---------")
    
    if options[menuEntryIdx] == options[0]:
        getMovieById()
    elif options[menuEntryIdx] == options[1]:
        pass
    elif options[menuEntryIdx] == options[2]:
        pass
    elif options[menuEntryIdx] == options[3]:
        pass
    elif options[menuEntryIdx] == options[4]:
        pass
    elif options[menuEntryIdx] == options[5]:
        pass
    elif options[menuEntryIdx] == options[6]:
        pass
    elif options[menuEntryIdx] == options[7]:
        print("Saliendo...\n")
        exit(0)
    else:
        print("Opción Desconocida!!!")
        exit(1)

if __name__ == "__main__":
    try:
        config = configparser.ConfigParser()
        config.read("movieDbCli.conf")
    except:
        print ("ERROR opening config file...!!!")
        exit(1)
    else:
        address = config["Conection"]["ADDRESS"]
        port = config["Conection"]["PORT"]
        global LOG_LEVEL
        LOG_LEVEL = int(config["Logging"]["LOGLEVEL"])

        global fullAddress
        fullAddress = address+":"+port+"/api/"
        printLog(DEBUG, "Address to connect: " + fullAddress + "\n")
        main()