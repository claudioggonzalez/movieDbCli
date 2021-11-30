#!/bin/python3

from simple_term_menu import TerminalMenu
import configparser
import json
import requests
from os import system as exec

def main(address):
    exec('clear')
    print (f"Address to connect: {address}\n")
    print ("OPTIONS:")
    print ("--------")
    options = ["Get Movie by ID","Get Movie by Title","Get Batch of Movies","Add Movie","Update Movie Data","Delete Movie", "API Info", "Exit"]
    menu = TerminalMenu(options)
    menuEntryIdx = menu.show()
    exec('clear')
    print(f"Has elegido la opcion: {menuEntryIdx} - {options[menuEntryIdx]}\n")
    if options[menuEntryIdx] == options[0]:
        pass
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
        print("Saliendo...")
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
    else:
        address = config["Conection"]["ADDRESS"]
        port = config["Conection"]["PORT"]
        fullAddress = address+":"+port+"/api/"
        main(fullAddress)