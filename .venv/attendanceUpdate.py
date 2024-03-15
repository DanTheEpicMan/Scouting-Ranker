import pandas as pd
import numpy as np
import time

possibleRounds = [1, 7, 13, 19, 25, 31, 37, 41, 53, 59, 61, 67]

def CurrentRoundGet():
    with open('currentRound.txt', 'r') as file:
        content = file.read()
        return content

def SearchByRound():
    CurrentRound = int(CurrentRoundGet())

    ScoutingRound = 0
    for i in range(CurrentRound, 0, -1):
        if i in possibleRounds:
            ScoutingRound = i
            break

    #Open the scouting app
    mydata = pd.read_csv("scoutingSchedual.csv")
    scoutSchedualArray = np.array(mydata)

    #Save the people who are scouting this round in a list
    ThisRoundScouting = []
    for i in range(len(scoutSchedualArray)):
        if scoutSchedualArray[i][0] == ScoutingRound:
            ThisRoundScouting.append(scoutSchedualArray[i][1])

    for i in range(len(ThisRoundScouting)):
        print(i, ThisRoundScouting[i])

    roundInput = "n/a"
    while (roundInput is not int):
        roundInput = input("Enter the number of the person you want to select: ")
        # try to convert to int
        try:
            roundInput = int(roundInput)
            break
        except ValueError:
            Print("Please enter a int (the round number")
    roundInput = int(roundInput)

    return ThisRoundScouting[roundInput]


def SearchByList():
    #Open the scouting app
    mydata = pd.read_csv("scoutingSchedual.csv")
    scoutSchedualArray = np.array(mydata)

    ListOfPeople = []

    #Make a list of people, avoid duplicates
    ListOfPeople = scoutSchedualArray[0][1]
    for i in range(len(scoutSchedualArray)):
        if scoutSchedualArray[i][1] not in ListOfPeople:
            ListOfPeople = np.append(ListOfPeople, scoutSchedualArray[i][1])

    for i in range(len(ListOfPeople)):
        print(i, ListOfPeople[i])

    roundInput = "n/a"
    while (roundInput is not int):
        roundInput = input("Enter the number of the person you want to select: ")
        # try to convert to int
        try:
            roundInput = int(roundInput)
            break
        except ValueError:
            Print("Please enter a int (the round number")
    roundInput = int(roundInput)

    return ListOfPeople[roundInput]

def ChangeAttendance(passedName, extra, absent):
    #Open the scouting app
    with open('scoutingPoints.csv', 'r+') as file:
        lines = file.readlines()
        file.seek(0)


        for line in lines:
            line = line.split(',')
            name = line[0]


            if passedName in name:
                line[3] = str(float(line[3]) + absent)
                line[4] = str(float(line[4]) + extra) + "\n"


            line = ','.join(line)

            # Delete all lines in the file to avoid errors
            file.truncate()

            file.write(line)




roundInput = "n/a"
print("""Select the option you want to do in relation to attendance:
1. No Change
2. Change attendance, selecting people from current scouting round
3. Change attendance, selecting people from entire list
""")
typeInput = input("Selection: ")
while (typeInput is not int):
    # try to convert to int
    try:
        typeInput = int(typeInput)
        break
    except ValueError:
        Print("Please enter a int (the round number")
typeInput = int(typeInput)

while (True):
    if typeInput == 1 or typeInput == 2 or typeInput == 3:
        break
    else:
        Print("Please enter numbers 1, 2, or 3")

personName = ""

if typeInput == 2:
    personName = SearchByRound()
elif typeInput == 3:
    personName = SearchByList()

if personName != (""):
    print("Have selected ", personName)
    roundInput = "n/a"
    print("""Select the option you want to do in relation to attendance:
    1.  Mark absent
    2.  Mark doing extra
    """)
    while (typeInput is not int):
        typeInput = input("Selection: ")
        # try to convert to int
        try:
            typeInput = int(typeInput)
            break
        except ValueError:
            Print("Please enter a int (the round number")
    typeInput = int(typeInput)

    if typeInput == 1:
        ChangeAttendance(personName, 0, -0.3)
    elif typeInput == 2:
        ChangeAttendance(personName, 0.15, 0)
