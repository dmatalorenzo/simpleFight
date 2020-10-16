import options
import champions

def endline():
    print("------------------------")

def blankLine():
    print("")

def welcome():
    blankLine()
    print("Welcome to Simple Fight")
    endline()

def gameOver():
    blankLine()
    #print("Thank you to play Simple Fight")  
    print("------ GAME  OVER ------")
    endline()

def printOptions(menu):
    blankLine()
    if menu == "mainMenu":
        mainMenuOptions()
    elif menu == "modifyMenu":
        modifyMenu()
    endline()

def mainMenuOptions():
    print("Choose an option to start:")
    print("1. Champions List")
    print("2. Champion Info")
    print("3. Fight")
    print("4. Manage champions")
    print("0. Exit ")

def modifyMenu():
    print("Choose an option to modify your champion:")
    print("1. Add Champions")
    print("2. Modify Champion")
    print("3. Remove Champion")
    print("0. Exit")

def championInfo(selectedChampion):
    blankLine()
    print(selectedChampion.name + ' stats: ')
    print('  --> Life:' + str(selectedChampion.life))
    print('  --> Attack:' + str(selectedChampion.attack))
    print('  --> Defence:' + str(selectedChampion.defence))
    print('  --> Speed:' + str(selectedChampion.speed))
    endline()

def championNotExist():
    print(name + ' is NOT added to the champions list.')

def championExist():
    print(name + ' is already added to the champions list.')

def updateChampion():
    print(' + Champions name: ')
    name = input()
    if championExist(name):
        dialogs.championNotExist()
    else:
        print(' + Stat to update:')
        life = input()
        print(' + New Value:')
        attack = input()
        champions.updateChampion(name, stat, value)

def printHit(champ1, champ2, damage):
    print(champ1.name, "hit", damage,  "to",  champ2.name)
    print(champ1.name, "       ", champ2.name)
    print(" ", champ1.life, "           ", champ2.life)
    print(" ^^^^^           ^^^^")
    print("(ง •̀_•́)ง --X-- ᕙ(⇀‸↼‶)ᕗ")
    endline()