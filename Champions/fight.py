import threading
from threading import Condition
import time

def battle(champ1, champ2):
    first = starter(champ1, champ2)
    if first == champ1:
        second = champ2
    else:
        second = champ1
    print("El primero en golpear es: " + first.name)
    firstHit = threading.Thread(target = fight, args = (first, second))
    secondHit = threading.Thread(target = fight, args = (second, first))
    firstHit.start()
    secondHit.start()

def starter(champ1, champ2):
    #Cuanto menos sea su variable speed, mas rapido pegaran. Pegan cada x speed segundos
    if champ1.speed < champ2.speed:
        return champ1
    if champ1.speed > champ2.speed:
        return champ2
    else:
        #random will start ... TODO
        return champ1

def fight(champ1, champ2):
    while bothAlive(champ1, champ2):
        hit(champ1, champ2)
    win = winner(champ1, champ2)
    if win.name == champ1.name:
        print("El ganador es:", win.name, "sobreviviendo con ", win.life, "HP")

def hit(champ1, champ2):
    damage = champ1.attack-champ2.defence
    champ2.life -= damage
    if champ2.life > 0:
        print(champ1.name, "hit", damage,  "to",  champ2.name, "(", champ2.life, ")")
    time.sleep(champ1.speed)

def alive(champ):
    if champ.life>0:
        return True
    else:
        return False

def bothAlive(champ1, champ2):
    if alive(champ1) and alive(champ2):
        return True
    else:
        return False

def winner(champ1, champ2):
    if champ1.life>champ2.life:
        return champ1
    else:
        return champ2
