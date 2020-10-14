import options
import champions
import fight
import dialogs

MAX_MAIN_OPTIONS = 4

champions.showChampionsList()

dialogs.welcome()

champ1 = champions.selectChampion("Renekton")
champ2 = champions.selectChampion("Irelia")

#fight.battle(champ1, champ2)

options.game(MAX_MAIN_OPTIONS)




