import fight
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

#Show a list with the names of the champions in the db
def showChampionsList():
    #Get the name of any champion into our champions table
    for x in getChampionList():
        #print champions names
        print( "--> " + x)

#Add a champion to the database
def addChampion(name, life, attack, defence, speed):
    #if we find a champion whith the same name into the db
    if tableChampions.search(User.name == name):
        #we output a message advicing that the champion is already created
        print(name + ' is already added to the champions list.')
        #print('To check the champions list try: championsList')
    #if the champion is not inte the db
    else:
        #the champion is inserted into the db
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

def getChampion(champ):
    champ = tableChampions.get(User.name == champ)
    selectedChamp = Champion(champ['name'],champ['life'], champ['attack'], champ['defence'], champ['speed'])
    return selectedChamp

def getChampionList():
    return [r['name'] for r in tableChampions]

def selectChampion(champ):
    print("El campeon seleccionado es: " + getChampion(selectedChamp.name))
    return selectedChamp

def championInfo(champion):
    selectedChampion = getChampion(champion)
    print(selectedChampion.name + ' stats: ')
    print'--> Life:' ,selectedChampion.life
    print'--> Attack:' ,selectedChampion.attack
    print'--> Defence:' ,selectedChampion.defence
    print'--> Speed:' ,selectedChampion.speed

def allChampionsInfo():
    for x in getChampionList():
        championInfo(x)

def updateChampion(champion, stat, value):
    tableChampions.update({stat:value}, User.name == champion)
    return getChampion(champion)

def removeChampion(champion):
    tableChampions.remove(User.name == champion)
