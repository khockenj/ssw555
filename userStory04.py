from datetime import datetime
import csv


def US_04():
    with open("families.csv", "r+") as fp:
        for line in fp.readlines():
            lineS = line.split(",")
            #print(lineS[2])

            if lineS[1] != "Married" and lineS[2] != "Divorced":
                bday = (datetime.strptime(lineS[1], '%d %b %Y'))
                dday = datetime.strptime(lineS[2], '%d %b %Y')
                if bday > dday:
                    print('ERROR: INDIVIDUAL: US04: ' + lineS[0] + ': Divorce ' + lineS[2] + ' Marriage ' + lineS[1])


(US_04())
