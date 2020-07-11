import champions
import fight

print("Welcome to Simple Fight")
print("Choose an option to start:")

print("1. Champions List")
print("2. Champion Info")
print("3. Fight")
print("4. Manage champions")



print("2. Add Champion")
print("3. Modify Champion")
print("4. Remove champion")


#Add champion to the list
champions.addChampion("Irelia", 150, 30, 5, 0.4)
#champions.addChampion("Renekton", 200, 20, 10, 0.5)

#Show the champions listy
print("Select a champion from the list")
champions.showChampionsList()

#Show champions information
#champions.championInfo("Irelia")
#champions.championInfo("Renekton")

#Show all the champions information
#champions.allChampionsInfo()

#Update champion information
#champions.updateChampion("Irelia", "speed", 0.3)
#champions.championInfo("Irelia")

#Remove a champion from the list
#champions.removeChampion("Irelia")





#champ1 = champions.selectChampion("Renekton")
#champ2 = champions.selectChampion("Amumu")

#fight.battle(champ1, champ2)
