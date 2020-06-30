import champions
import fight


print("Selecciona un campeon de la lista")
champions.showChampionsList()

#champions.addChampion("Amumu", 180, 25, 15, 0.4)
#champions.addChampion("Renekton", 200, 20, 10, 0.5)

champ1 = champions.setChampion("Irelia")
champ2 = champions.setChampion("Amumu")


fight.battle(champ1, champ2)
