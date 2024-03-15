###### Settings ######
#More points = less chance to be picked

#Points awarded to try to stop people from serving back to back
LastRoundScoutedPoints = '1.0'

#Points awareded so people who are currently scouting
# to not currently scout (cant cout 2x at the same time)
ThisRoundScoutingPoints = '100.0'

#Points awarded to try to stop people from serving back to back
NextRoundScoutingPoints = '1.0'
######## End #########

import pandas as pd
import numpy as np

#Name, Points for year, Points for Last round scouted, Abcense Penalty, Abcense Fillin Points

def CurrentRoundSet(round):
    try:
        round = int(round)
        with open('currentRound.txt', 'r+') as file:
            #content = file.read()
            file.seek(0)
            file.write(str(round))
        return True
    except ValueError:
       return False
    
def CurrentRoundGet():
    with open('currentRound.txt', 'r') as file:
        content = file.read()
        return content

def SetPointsForRound():
    #Get the data from the csv file
    mydata = pd.read_csv("scoutingSchedual.csv")
    scoutSchedualArray = np.array(mydata)
    
    #Get current round
    currentRound = int(CurrentRoundGet())

    possibleRounds = [1, 7, 13, 19, 25, 31, 37, 41, 53, 59, 61, 67]

    #Make a loop that subtracts 1 from currentRound until one of the numbers in PossibelRounds is hit, then save the round it hit
    ScoutingRound = 0
    for i in range(currentRound, 0, -1):
        if i in possibleRounds:
            ScoutingRound = i
            break

    PerviousScoutingRound = ScoutingRound - 6
    NextScoutingRound = ScoutingRound + 6

    #Save the people who scouted in the last round in list
    LastRoundScouted = []
    for i in range(len(scoutSchedualArray)):
        if scoutSchedualArray[i][0] == PerviousScoutingRound:
            LastRoundScouted.append(scoutSchedualArray[i][1])

    #Save the people who are scouting this round in a list
    ThisRoundScouting = []
    for i in range(len(scoutSchedualArray)):
        if scoutSchedualArray[i][0] == ScoutingRound:
            ThisRoundScouting.append(scoutSchedualArray[i][1])

    #Save the people who are souting the next round in list
    NextRoundScouting = []
    for i in range(len(scoutSchedualArray)):
        if scoutSchedualArray[i][0] == NextScoutingRound:
            NextRoundScouting.append(scoutSchedualArray[i][1])

    # Open scouting points file, loop through every line
    with open('scoutingPoints.csv', 'r+') as file:
        lines = file.readlines()
        file.seek(0)

        # If the names of the people are in LastRoundScouted, set the points in "Points for Last round scouted" to 1
        for line in lines:
            
            line = line.split(',')
            name = line[0]
            #skip line 1
            if name == "Name":
                line = ','.join(line)
                file.write(line)
                continue
            
            if name in LastRoundScouted:
                line[2] = LastRoundScoutedPoints
            # If the names of the people are in ThisRoundScouting, set the points in "Points for Last round scouted" to 100
            elif name in ThisRoundScouting:
                line[2] = ThisRoundScoutingPoints
            elif name in NextRoundScouting:
                line[2] = NextRoundScoutingPoints
            # If the names of the people are not in ThisRoundScouting, set the points in "Points for Last round scouted" to 0
            else:
                line[2] = '0'

            line = ','.join(line)

            # Delete all lines in the file to avoid errors
            file.truncate()

            file.write(line)

roundInput = "n/a"
while (roundInput is not int):
    roundInput = input("Enter current round (or enter 0 to keep current one): ")
    #try to convert to int
    try:
        roundInput = int(roundInput)
        break
    except ValueError:
        Print("Please enter a int (the round number")

#checks that round is not 0
if roundInput != 0:
    CurrentRoundSet(int(roundInput))
    SetPointsForRound()

print("Now set to round ", CurrentRoundGet())
