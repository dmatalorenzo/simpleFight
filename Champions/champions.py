import fight
import options
import dialogs
from tinydb import TinyDB
from tinydb import Query

db = TinyDB('champions.json')
tableChampions = db.table('champions')
User = Query()

class Champion:
    def __init__(self, name, life, attack, defence, speed):
        self.name=name
        self.life=life
        self.attack=attack
        self.defence = defence
        self.speed=speed

def showChampionsList():
    for championName in getChampionList():
        print( "--> " + championName)
    dialogs.endline()

def getChampion(champ):
    champ = tableChampions.get(User.name == champ)
    selectedChamp = Champion(champ['name'],champ['life'], champ['attack'], champ['defence'], champ['speed'])
    return selectedChamp

def getChampionList():
    return [r['name'] for r in tableChampions]

def selectChampion(champ):
    champion = getChampion(champ)
    print("El campeon seleccionado es: " + champion.name)
    return champion

def championInfo(champion):
    selectedChampion = getChampion(champion)
    dialogs.championInfo(selectedChampion)

def allChampionsInfo():
    for x in getChampionList():
        championInfo(x)

def addChampion():
    print(' + Champions name: ')
    name = input()
    if championExist(name):
        print(name + ' is already added to the champions list.')
    else:
        print(' + Life Stat:')
        life = input()
        print(' + Attack Stat:')
        attack = input()
        print(' + Defence Stat:')
        defence = input()
        print(' + Speed Stat:')
        speed = input()

        tableChampions.insert(
            {
              "name": name,
              "life": life,
              "attack": attack,
              "defence": defence,
              "speed": speed,
            }
        )
        print("Champion added: " + name)

def updateChampion(champion, stat, value):
    tableChampions.update({stat:value}, User.name == champion)
    return getChampion(champion)

def removeChampion(champion):
    tableChampions.remove(User.name == champion)

def championExist(name):
    if tableChampions.search(User.name == name):
        return True
    else:
        return False