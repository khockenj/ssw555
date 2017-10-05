#So, put all of your methods in this file, and if you want to call them in the gedcom2csv call it as meths.METHODNAME
import warnings
import csv
from datetime import datetime

def afterCurrentDate(d1):
	if d1 > datetime.today().date():
		warnings.warn('Date ' + str(d1) + ' is after the current date')
		return True #invalid date
	elif d1 < datetime.today().date():
		return False
	else:
		warnings.warn('Date ' + str(d1) + ' is an invalid date')
		return True

def days_difference(d1, d2):
	#ignoring d2, as it's the current date anyway
	if afterCurrentDate(d1):
		warnings.warn('The date is after the current date')
		return -1
	else:
		return (d2-d1).days

def birthBeforeMarriage():
	err = []
	with open('families.csv') as file1:
		file1.readline()
		for row in csv.reader(file1, delimiter=','):
			married =  datetime.strptime(row[1], '%d %b %Y').date()
			husb = row[3]
			wife = row[5]
			div =  datetime.strptime(row[2], '%d %b %Y').date()
			with open('individuals.csv') as file2:
				file2.readline()
				birthH = '??-??-????'
				birthW = '??-??-????'
				for row2 in csv.reader(file2,delimiter=','):
					if husb in row2:	#Pretty sure alot of the user stories are basic if statements in here then we can make it a more generic method name
						birthH =  datetime.strptime(row2[3], '%d %b %Y').date()
						if(row2[4] != "Alive"):
							deathH =  datetime.strptime(row2[4], '%d %b %Y').date()
					if wife in row2:
						birthW =  datetime.strptime(row2[3], '%d %b %Y').date()
						if(row2[4] != "Alive"):
							deathW =  datetime.strptime(row2[4], '%d %b %Y').date()
			if birthH > married:
				err.append(husb + "'ss birthday (" + str(birthH) + ') is before his marriage date (' + str(married) + ')')
			if birthW > married:
				err.append(wife + "'s birthday (" + str(birthW) + ') is before her marriage date (' + str(married) + ')')
			if deathH != "Alive" and deathH < birthH:
				err.append(husb + "'s death(" + str(deathH) + ")is before his birth ( " + str(birthH) + ")")
			if deathW != "Alive" and deathW < birthW:
				err.append(wife + "'s death(" + str(deathW) + ")is before his birth ( " + str(birthW) + ")")
			#User Story 05 Marriage before death and divorce before death

			if deathH < married:
				err.append(husb + "'s death date(" + str(deathH) + ") is before marriage date(" + str(married) + ")")
			if deathH < div:
				err.append(husb + "'s death date(" + str(deathH) + ") is before divorce date(" + str(div) + ")")
			if deathW < married:
				err.append(wife + "'s death date(" + str(deathW) + ") is before marriage date(" + str(married) + ")")
			if deathW < div:
				err.append(wife + "'s death date(" + str(deathW) + ") is before divorce date(" + str(div) + ")")
	return err

def US_03():
    with open("individuals.csv", "r+") as fp:
        for line in fp.readlines():
            lineS = line.split(",")
            #print(lineS[3])

            if lineS[4] != "Alive" and lineS[4] != "Death":
                bday = (datetime.strptime(lineS[3], '%d %b %Y'))
                dday = datetime.strptime(lineS[4], '%d %b %Y')
                if bday>dday:
                      print('ERROR: INDIVIDUAL: US03: ' + lineS[0] + ': Death ' + lineS[4] + ' before birth ' + lineS[3])

def US_08():
    with open("families.csv","r+") as fp:
        family_id = []
        indi_id = []
        marriage_dates = []

        for line in fp.readlines():
            lineS = line.split(',')
            family_id.append(lineS[0])
            indi_id.append(lineS[7])
            marriage_dates.append((lineS[1]))

    family_id = family_id[1:]
    indi_id = indi_id[1:]
    marriage_dates= marriage_dates[1:]
    family_to_indv = dict(zip(family_id, indi_id))
    familt_to_marriage = dict(zip(family_id,marriage_dates))


    id_to_birthdates = {}
    with open('individuals.csv','r+') as fp1:
        for line in fp1.readlines():
            lineS = line.split(',')
            for i in family_to_indv.values():
                if lineS[0] in i:
                    id_to_birthdates[lineS[0]]= lineS[3]

    mardate = []
    bday = []
    for k,v in family_to_indv.items():
        if familt_to_marriage.get(k) != 'NA':
            for l,m in id_to_birthdates.items():
                if l in v:
                    bday = m
                    mardate = familt_to_marriage.get(k)
                    if(datetime.strptime(bday, '%d %b %Y') < datetime.strptime(mardate, '%d %b %Y')) :
                            print('ERROR: INDIVIDUAL: US08: ' + l +
                              ': Child Birth ' + bday + ' before parents ' + k +
                              ' marriage ' + mardate)


def marriage_before_divorce():
    with open("families.csv", "r+") as fp:
        for line in fp.readlines():
            lineS = line.split(",")
            #print(lineS[2])

            if lineS[1] != "Married" and lineS[2] != "Divorced":
                bday = (datetime.strptime(lineS[1], '%d %b %Y'))
                dday = datetime.strptime(lineS[2], '%d %b %Y')
                if bday > dday:
                    print('ERROR: INDIVIDUAL: US04: ' + lineS[0] + ': Divorce ' + lineS[2] + ' Marriage ' + lineS[1])


