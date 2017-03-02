import csv
#name of file
file = "csvChallenge.csv"
with open(file,"r") as guestList:
    allData = csv.reader(guestList)

    for currentRow in allData:
        print(",".join(currentRow))
    