import champions
import dialogs
import fight
from tinydb import TinyDB
from tinydb import Query

MAX_MODIFY_OPTIONS = 3

def game(maxOptions):
    endGame = False
    while not endGame:
        endGame = options(maxOptions, "mainMenu")    
    dialogs.gameOver()

def options(maxOptions, menu):
    validOption=False
    while not validOption:
        dialogs.printOptions(menu)
        option=int(input())
        if option <= maxOptions and option > 0:
            validOption = True
        elif option == 0:
            return True
        else:
            print("Selecciona una opcion valida")
        dialogs.endline()        
    action(option, menu)
    
def action(option, menu):
    if menu == "mainMenu":
        actionMainMenu(option)
    elif menu == "modifyMenu":
        actionModifyMenu(option)

def actionMainMenu(option):
    if option == 0:
        exit
    elif option == 1:
        champions.showChampionsList()
    elif option == 2:
        print("Que campeon quieres seleccionar?")
        champ = input()
        champions.championInfo(champ)
    if option == 3:
        fight.chooseFighters()

    if option == 4:
        options(MAX_MODIFY_OPTIONS, "modifyMenu")

def actionModifyMenu(option):
    if option == 0:
        exit
    elif option == 1:
        champions.addChampion()
    elif option == 2:
        print("Choose a champion to modify")
        champ = input()
        champions.championInfo(champ)
    elif option == 3:
        print("Choose a champion to remove")
        champ = input()
        champions.removeChampion(champ)
       
#Champions list
def championList():
    champions.showChampionsList()

#Champion Info
def championInfo():

    while True:
        seeList = input("Do you wanna see the champions list? (Y/N) ")
        print(seeList)
        if seeList == "Y":
            champions.showChampionsList()
            break
        elif seeList == "N":
            break
        else:
            seeList = input("Introduce a correct value: ")

    champion = input("Introduce the champion name: ")

