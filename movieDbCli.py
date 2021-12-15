#!/bin/python3

from typing import Optional
from simple_term_menu import TerminalMenu
import configparser
import json
import requests
from texttable import Texttable

DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3
CRITICAL = 4

def printLog(msgLogLevel, logMessage):
    if msgLogLevel >= LOG_LEVEL:
        print(logMessage)

def getMovieById(id = -1):
    if id == -1:
        options = ["[1]Define ID to get","[0]Return MAIN MENU"]
        menuEntryIdx = displayMenu(options, "GET MOVIE BY ID:\n-----------------")

        if options[menuEntryIdx] == options[0]:
            id = int(input("Movie ID: "))
        elif options[menuEntryIdx] == options[1]:
            main()
        else:
            print("Unknown option!!!")
            exit(1)
    
    response = requests.get(fullAddress+"getId/"+str(id)+"/")
    printLog(DEBUG, "Status Code: "+str(response.status_code))
    printLog(DEBUG, "Data: "+response.text+"\n")
    
    if response.status_code == 200:
        showFullTable(response.json())
    else:
        print("ERROR!!! Code: " + str(response.status_code))


def getMovieByTitle(title = ""):
    if title == "":
        options = ["[1]Define Title to get","[0]Return MAIN MENU"]
        menuEntryIdx = displayMenu(options, "GET MOVIE BY TITLE:\n--------------------")

        if options[menuEntryIdx] == options[0]:
            title = input("Movie Title: ")
        elif options[menuEntryIdx] == options[1]:
            main()
        else:
            print("Unknown option!!!")
            exit(1)
    
    response = requests.get(fullAddress+"getTitle/"+title+"/")
    printLog(DEBUG, "Status Code: "+str(response.status_code))
    printLog(DEBUG, "Data: "+response.text+"\n")
    
    if response.status_code == 200:
        showFullTable(response.json())
    else:
        print("ERROR!!! Code: " + str(response.status_code))

def getMovieBatch():
    options = ["[1]Get Movie Batch","[0]Return MAIN MENU"]
    menuEntryIdx = displayMenu(options, "GET MOVIE BATCH:\n---------------")

    if options[menuEntryIdx] == options[0]:
        response = requests.get(fullAddress+"getBatch")
        printLog(DEBUG, "Status Code: "+str(response.status_code))
        printLog(DEBUG, "Data: "+response.text+"\n")
        
        if response.status_code == 200:
            #showBatchTable(response.json())
            pass
        else:
            print("ERROR!!! Code: " + str(response.status_code))
    
    elif options[menuEntryIdx] == options[1]:
        main()
    else:
        print("Unknown option!!!")
        exit(1)

def addMovie():
    options = ["[1]Input Movie Data","[0]Return MAIN MENU"]
    menuEntryIdx = displayMenu(options, "INPUT MOVIE DATA:\n----------------")

    if options[menuEntryIdx] == options[0]:
        data = inputMovieData()
        # POST resquests

    elif options[menuEntryIdx] == options[1]:
        main()
    else:
        print("Opción Desconocida!!!")
        exit(1)

def inputMovieData(_data = {"title":"",
                            "altTitle":"",
                            "year":0,
                            "originCountry":"",
                            "releaseDate":"",
                            "downloadDate":"",
                            "subtitle":False,
                            "status":0}):
    if _data["title"]:

        while (_data["title"] == ""):
            _data["title"] = input("Title (mandatory):")
            
        _data["altTitle"] = input("Alternative Title: ")
        
        while (_data["year"] < 1900 or _data["year"] > 2100):
            _data["year"] = int(input("Year [YYYY] (mandatory):"))
            
        _data["originCountry"] = input("Country of Origin: ")
        
        _data["releaseDate"] = input("Release Date (YYYY-MM-DD): ")
        
        _data["downloadDate"] = input("Release Date (YYYY-MM-DD): ")
        
        _subtitleTxt = input("Has subtitles? (y/N):")
        
        if (_subtitleTxt == "y"):
            _data["subtitle"] = True

        _statusOpt = ["[0] Recorded","[1] Downloaded","[2] Pending","[3] Seen"]
        _data["status"] = displayMenu(_statusOpt)
        
    else:
        
        _data["title"] = validateStr("Title", _data["title"])
        
        _data["altTitle"] = validateStr("Alternative Title", _data["altTitle"])
        
        _data["year"] = validateInt("Year", _data["year"])
        
        _data["originCountry"] = validateStr("Country of Origin", _data["originCountry"])
        
        _data["releaseDate"] = validateStr("Release Date (YYYY-MM-DD)", _data["releaseDate"])
        
        _data["downloadDate"] = validateStr("Download Date (YYYY-MM-DD)", _data["downloadDate"])
        
        _data["subtitle"] = validateBool("Has subtitles? (y/n)", _data["subtitle"])
        
        _options = ["[0]Recorded","[1]Downloaded","[2]Pending","[3]Seen"]
        _data["status"] = TerminalMenu(_options, "Movie status:\n---------", cursor_index = _data["status"])

    return _data

def validateStr(label, data):
	value = data
	_str = label + " [" + data + "]:"
	_temp = input(_str)

	if _temp:
		value = _temp

	return value

def validateInt(label, data):
	value = data
	_str = label + " [" + str(data) + "]:"
	_temp = input(_str)

	if _temp:
		value = int(_temp)

	return value

def validateBool(label, data):

	if int(data):
		_str = "Yes"
	else:
		_str = "No"

	_temp = input(label + " [" + _str + "]:")

	if _temp == "":
		return int(data)
	elif _temp == "yes" or _temp == "Yes":
		return True
	else:
		return False

def updateMovie():
    options = ["[1]Define ID to get","[0]Return MAIN MENU"]
    menuEntryIdx = displayMenu(options, "UPDATE MOVIE BY ID:\n-------------------")

    if options[menuEntryIdx] == options[0]:
        id = int(input("Movie ID: "))
        #PUT requests
        #Show movie data from request and ask for modificactions
        pass
    elif options[menuEntryIdx] == options[1]:
        main()
    else:
        print("Unknown option!!!")
        exit(1)

def deleteMoviebyId():
    options = ["[1]Define ID to delete","[0]Return MAIN MENU"]
    menuEntryIdx = displayMenu(options, "DELETE MOVIE BY ID:\n-------------------")

    if options[menuEntryIdx] == options[0]:
        id = int(input("Movie ID: "))
        #DELETE requests
        #Show movie data from request and ask for modificactions
        pass
    elif options[menuEntryIdx] == options[1]:
        main()
    else:
        print("Unknown option!!!")
        exit(1)

def getApiInfo():
    response = requests.get(fullAddress)
    table = Texttable()

def displayMenu(options, menuTitle = ""):
    menu = TerminalMenu(options, title=menuTitle)
    idx = menu.show()
    return idx

def showFullTable(dataList):
    data = dataList[0]
    hasSubs = lambda x: "Yes" if x == 1 else "No"
    null2empty = lambda x: x if x != None else "-"
    table = Texttable()
    table.add_rows([["ITEM","VALUE"],
                    ["ID",data["id"]],
                    ["Title",data["title"]],
                    ["Alternative Title",null2empty(data["altTitle"])],
                    ["Year",data["year"]],
                    ["Country of Origin",null2empty(data["originCountry"])],
                    ["Release Date",null2empty(data["releaseDate"])],
                    ["Download Date",null2empty(data["downloadDate"])],
                    ["Subtitles",hasSubs(data["subtitle"])],
                    ["Status",data["status"]]])
    print(table.draw())
    print("\n")

def main():
    options = ["[1]Get Movie by ID","[2]Get Movie by Title","[3]Get Batch of Movies","[4]Add Movie","[5]Update Movie Data","[6]Delete Movie", "[7]API Info", "[0]Exit"]
    menuEntryIdx = displayMenu(options, "MAIN MENU:\n---------")

    if options[menuEntryIdx] == options[0]:
        getMovieById()
    elif options[menuEntryIdx] == options[1]:
        getMovieByTitle()
    elif options[menuEntryIdx] == options[2]:
        getMovieBatch()
    elif options[menuEntryIdx] == options[3]:
        addMovie()
    elif options[menuEntryIdx] == options[4]:
        updateMovie()
    elif options[menuEntryIdx] == options[5]:
        deleteMoviebyId()
    elif options[menuEntryIdx] == options[6]:
        getApiInfo()
        pass
    elif options[menuEntryIdx] == options[7]:
        print("Exit...\n")
        exit(0)
    else:
        print("Unknown option!!!")
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
        fullAddress = "http://"+address+":"+port+"/api/"
        printLog(DEBUG, "Address to connect: " + fullAddress + "\n")
        main()
