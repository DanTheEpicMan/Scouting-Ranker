#In the file scoutingchedual.csv, get the names of everyone (column 1) and the year they are (column 2) (starts at collum 0)

#Put there names into scoutingPoints.csv in colum 0
#Get there year and assign the correct amount of points
#Fr = 1
#So = 2
#Jr = 3
#Sr = 4
import pandas as pd
import numpy as np

#Get the data from the csv file
mydata = pd.read_csv("scoutingSchedual.csv")
scoutSchedualArray = np.array(mydata)

#Open scouting points file, write the names of the people in first column, and the year as points in the second column
scoutingPoints = open("scoutingPoints.csv", "w")
scoutingPoints.write("Name, Points for year, Points for Last round scouted, Abcense Penalty, Abcense Fillin Points\n") #remember to skip first line

for i in range(len(scoutSchedualArray)):
    #Get the name of the person
    toWrite = str(scoutSchedualArray[i][1])
    #Get the year of the person, remove quotes
    year = scoutSchedualArray[i][2]
    year = year[2:-1]
    #Write the name and year to the scoutingPoints file
    if year == "Fr":
        toWrite += ", 1.0, "
    elif year == "So":
        toWrite += ", 2.0, "
    elif year == "Jr":
        toWrite += ", 3.0, "
    elif year == "Se":
        toWrite += ", 4.0, "

    #Write the rest of the data to the file
    toWrite += "0.0, 0.0, 0.0\n"
    scoutingPoints.write(toWrite)
