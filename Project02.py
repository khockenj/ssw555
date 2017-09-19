#Rob Weiss 09.12.17

#Open File
with open("GEDCOM Data v2.ged", 'r') as testFile:
    for line in testFile:
        print("--> " + line)
        currentLine = (line.rstrip()).split(" ")
        #Check if valid
        valid = "N"
        #Level 0
        if currentLine[0] == "0":
            if currentLine[1] == "HEAD" or currentLine[1] == "NOTE" or currentLine[1] == "TRLR":
                valid = "Y"
            elif currentLine[2] == "FAM" or currentLine[2] == "INDI":
                valid = "Y"
        #Level 1
        if currentLine[0] == "1":
            if currentLine[1] == "BIRT" or currentLine[1] == "CHIL" or currentLine[1] == "DEAT" or currentLine[1] == "DIV" or currentLine[1] == "FAMC" or currentLine[1] == "FAMS" or currentLine[1] == "HUSB" or currentLine[1] == "MARR" or currentLine[1] == "NAME" or currentLine[1] == "SEX" or currentLine[1] == "WIFE":
                valid = "Y"
        #Level 2
        if currentLine[0] == "2":
            if currentLine[1] == "DATE":
                valid = "Y"
        #Output
        print("<-- " + currentLine[0] + "|" + currentLine[1] + "|" + valid + "|", end='')
        y = 2
        for x in (currentLine[2:]):
            print(currentLine[y], end=' ')
            y = y + 1
        print()
