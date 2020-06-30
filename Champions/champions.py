import fight
from tinydb import TinyDB
from tinydb import Query

db = TinyDB('./champions.json')
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
    championsList = [r['name'] for r in tableChampions]
    for x in championsList:
        print( "--> " + x)

def addChampion(name, life, attack, defence, speed):
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

def setChampion(champ):
    champ = tableChampions.search(User.name == champ)
    for x in champ:
        selectedChamp = Champion(x['name'],x['life'], x['attack'], x['defence'], x['speed'])
    print("El campeon seleccionado es: " + selectedChamp.name)
    return(selectedChamp)
