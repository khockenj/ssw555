#So, put all of your methods in this file, and if you want to call them in the gedcom2csv call it as meths.METHODNAME
import warnings
import csv
from datetime import datetime, timedelta

def afterDate(d1,d2):
	if d1 > d2:
		return True #invalid date
	elif d1 < d2:
		return False
	else:
		return True

def days_difference(d1, d2):
	#ignoring d2, as it's the current date anyway
	if afterDate(d1,d2):
		return -1
	else:
		return (d2-d1).days

def birthBeforeMarriage():
	err = []
	today = datetime.today().date()
	with open('families.csv') as file1:
		file1.readline()
		for row in csv.reader(file1, delimiter=','):
			try:
				married = datetime.strptime(row[1], '%d %b %Y').date()
				div =  datetime.strptime(row[2], '%d %b %Y').date()
			except:
				married = datetime.today().date()
				div = datetime.today().date()
			husb = row[3]
			wife = row[5]
			with open('individuals.csv') as file2:
				file2.readline()
				birthH = '??-??-????'
				birthW = '??-??-????'
				for row2 in csv.reader(file2,delimiter=','):
					if husb in row2:	#Pretty sure alot of the user stories are basic if statements in here then we can make it a more generic method name
						birthH =  row2[3]
						deathH =  row2[4]
					if wife in row2:
						birthW =  row2[3]
						deathW =  row2[4]
				if deathH != "Alive" and birthH != "??-??-????":
					birthH = datetime.strptime(birthH, '%d %b %Y').date()
					deathH = datetime.strptime(deathH, '%d %b %Y').date()
				if deathW != "Alive" and birthW != "??-??-????":
					birthW = datetime.strptime(birthW, '%d %b %Y').date()
					deathW = datetime.strptime(deathW, '%d %b %Y').date()
			#Birth before marriage, death before marriage
			if married != today:	#to account for date=today for bad marriage dates
				if birthH > married:
					err.append("ERROR: US02: " + husb + "'s birth date (" + str(birthH) + ') is before his marriage date (' + str(married) + ')')
				if birthW > married:
					err.append("ERROR: US02: " + wife + "'s birth date (" + str(birthW) + ') is before her marriage date (' + str(married) + ')')
				if deathH != "Alive" and deathH < birthH:
					err.append("ERROR: US03: " + husb + "'s death(" + str(deathH) + ") is before his birth ( " + str(birthH) + ")")
				if deathW != "Alive" and deathW < birthW:
					err.append("ERROR: US03: " + wife + "'s death(" + str(deathW) + ") is before her birth ( " + str(birthW) + ")")
				#User Story 05 Marriage before death and divorce before death
			if div != today:
				if deathH < married:
						err.append("ERROR: US05: " + husb + "'s death date(" + str(deathH) + ") is before marriage date(" + str(married) + ")")
				if deathH < div:
						err.append("ERROR: US06: " + husb + "'s death date(" + str(deathH) + ") is before divorce date(" + str(div) + ")")
				if deathW < married:
						err.append("ERROR: US05: " + wife + "'s death date(" + str(deathW) + ") is before marriage date(" + str(married) + ")")
				if deathW < div:
						err.append("ERROR: US06: " + wife + "'s death date(" + str(deathW) + ") is before divorce date(" + str(div) + ")")
			if married != today or today != div:
				if afterDate(birthH,today):
					err.append("ERROR: US01: " + husb  + "'s death date(" + str(birthH) + ") is after today(" + str(today) + ")")
				if afterDate(birthW,today):
					err.append("ERROR: US01:" + wife + "'s death date(" + str(birthW) + ") is after today" + str(today) + ")")
				if afterDate(deathH,today):
					err.append("ERROR: US01: " + husb  + "'s death date(" + str(birthH) + ") is after today(" + str(today) + ")")
				if afterDate(deathW,today):
					err.append("ERROR: US01: " + wife + "'s death date(" + str(birthW) + ") is after today" + str(today) + ")")
				if afterDate(div,today):
					err.append("ERROR: US01: " + husb + "and " + wife + "'s divorce date(" + str(div) + ") is before the current date(" + str(today) + ")")
				if afterDate(married,today):
					err.append("ERROR: US01: " + husb + "and " + wife + "'s marriage date(" + str(div) + ") is before the current date(" + str(today) + ")")

				
			else:
				err.append("ERROR: GENERAL: Marriage date for " + husb  + " and " + wife + " not available")
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
        if familt_to_marriage.get(k) != 'Years not provided':
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

            if lineS[1] != "Married" and lineS[2] != "Years not provided":
                mday = (datetime.strptime(lineS[1], '%d %b %Y'))
                dday = datetime.strptime(lineS[2], '%d %b %Y')
                if mday > dday:
                    print('ERROR: INDIVIDUAL: US04: ' + lineS[0] + ': Divorce ' + lineS[2] + ' Marriage ' + lineS[1])

def birth_before_parents_died():
    with open("families.csv", "r+") as fp:
        family_id = []
        indi_id = []
        father_id = []
        mother_id = []


        for line in fp.readlines():
            lineS = line.split(',')
            family_id.append(lineS[0])
            indi_id.append(lineS[7])
            father_id.append(lineS[3])
            mother_id.append(lineS[5])

    family_id = family_id[1:]
    indi_id = indi_id[1:]
    father_id = indi_id[1:]
    mother_id = indi_id[1:]

    family_to_indv = dict(zip(family_id, indi_id))
    family_to_father_id = dict(zip(family_id, father_id))
    family_to_mother_id = dict(zip(family_id, mother_id))


    id_to_birthdates_child = {}

    with open('individuals.csv','r+') as fp1:
        for line in fp1.readlines():
            lineS = line.split(',')
            for i in family_to_indv.values():
                if lineS[0] in i:
                    id_to_birthdates_child[lineS[0]]= lineS[3]

    id_to_deathdates_father = {}

    with open('individuals.csv', 'r+') as fp1:
        for line in fp1.readlines():
            lineS = line.split(',')
            for i in family_to_father_id.values():
                if lineS[0] in i:
                    id_to_deathdates_father[lineS[0]] = lineS[4]

    id_to_deathdates_mother = {}

    with open('individuals.csv', 'r+') as fp1:
        for line in fp1.readlines():
            lineS = line.split(',')
            for i in family_to_mother_id.values():
                if lineS[0] in i:
                    id_to_deathdates_mother[lineS[0]] = lineS[4]

    fddate = []
    mddate =[]
    mddate = []


    for k,v in family_to_indv.items():
        if family_to_mother_id.get(k) != 'NA':
            for l,m in id_to_deathdates_mother.items():
                if l in v:
                    mddate.append(m)

    mom_death = dict(zip(family_id, mddate))

    for k,v in family_to_indv.items():
        if family_to_mother_id.get(k) != 'NA':
            for l,m in id_to_deathdates_father.items():
                if l in v:
                    fddate.append(m)

    dad_death = dict(zip(family_id, mddate))

    flag1 = 0
    flag2 = 0
    for k,v in family_to_indv.items():
        if mom_death.get(k) != 'NA':
            for l,m in id_to_birthdates_child.items():
                if l in v:
                    bday = m
                    mardate = mom_death.get(k)
                    if(datetime.strptime(bday, '%d %b %Y') > datetime.strptime(mardate, '%d %b %Y')) :
                            flag1 = 1


    for k,v in family_to_indv.items():
        if dad_death.get(k) != 'NA':
            for l,m in id_to_birthdates_child.items():
                if l in v:
                    bday2 = m
                    mardate2 = dad_death.get(k)
                    if(datetime.strptime(bday, '%d %b %Y') > (datetime.strptime(mardate2, '%d %b %Y') + timedelta(days=270))):
                            flag2 = 1

    if flag1==1 & flag2==1:
        print('ERROR: INDIVIDUAL: US09: Child Birth Before parents died')
