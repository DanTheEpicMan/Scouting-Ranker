# 1. Setup scoutingSchedual manualy
# 2. Run the setup script
# 3. Run this file

import os

#Runs round update
os.system("python RoundUpdate.py")

#Runs attendance update
os.system("python attendanceUpdate.py")

#Runs the setupLeaderboad file
os.system("python setupLeaderboard.py")




#Outline
# Make an algorithem that will dtermin who should scout next
#Group = 6 rounds


# Things to consider 
# 1. Year of each person
# - Freshman 4, Softmore 3, Junior 2, Senior 1
# 2. Rounds since last scouted
# - If they just scouted 2pt, 1pt for scouted last, +100 for now scouting
# 3. Abcense penalty
# - For every round missed, -0.3
# 4. Time till next round (double duty)
# - If about to scout + 2pt, 1pt for scouting in a round
# 5. Amount of absences filled
# - For every round filled, +0.15

#"Name", Points for year, Points for Last round scouted, Abcense Penalty, Scouting next round, Abcense Fillin Points

