#Rob Weiss 09.12.17
#TEST
#Open File
with open("GEDCOM Data.ged", 'r') as testFile:
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
            if currentLine[1] in ["BIRT", "CHIL", "DEAT", "DIV", "FAMC", "FAMS", "HUSB", "MARR", "NAME", "SEX", "WIFE"]:
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
