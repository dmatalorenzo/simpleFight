import champions
from tinydb import TinyDB
from tinydb import Query

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

#Fight
#def fight():

#Manage Champion
#def manageChampion():

#def switchOptions(argument):
#    switcher = {
#
#    }
#    print switcher.get(argument, "Invalid option")
