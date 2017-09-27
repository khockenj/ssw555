#Rob Weiss - User Story 01

from datetime import datetime

def afterCurrentDate(aDate):
    if aDate > datetime.today():
        print("Invalid date specified. " + gedcomDate.strftime("%d %b %Y") + "is after the current date.")
        return 1

#Open File
with open("userStory1DummyData.ged", 'r') as testFile:
    for line in testFile:
        currentLine = (line.rstrip()).split(" ")
        if currentLine[1] in ["DATE"]:
            gedcomDate = datetime.strptime(currentLine[2] + currentLine[3] + currentLine[4], "%d%b%Y")
            afterCurrentDate(gedcomDate)
