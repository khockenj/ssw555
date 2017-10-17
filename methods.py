#So, put all of your methods in this file, and if you want to call them in the gedcom2csv call it as meths.METHODNAME
import warnings
import csv
import datetime

def afterDate(d1, d2):
	if not isinstance(d1, datetime.date):
		d1 = datetime.datetime.strptime(d1, '%d %b %Y').date()
	if not isinstance(d2, datetime.date):
		d2 = datetime.datetime.strptime(d2, '%d %b %Y').date()
	if d1 > d2:
		return True #invalid date
	elif d1 < d2:
		return False
	else:
		return True

def days_difference(d1, d2, type):
	if afterDate(d1,d2):
		return -1
	else:
		typeDict = {'years': 365, 'weeks': 7, 'months': 30.4, 'days': 1}
		return str(((d2-d1)/typeDict[type]).days)
		
def test_US27():
	birthday = datetime.datetime(1900,5,10).date()
	assert int(days_difference(birthday,today,'years')) == 117
#def test_US13():

def INDI_FAM_relations():
	err = []
	today = datetime.datetime.today().date()
	with open('families.csv') as file1:
		file1.readline()
		for row in csv.reader(file1, delimiter=','):
			try:
				married = datetime.datetime.strptime(row[1], '%d %b %Y').date()
			except:
				married = datetime.datetime(1, 1, 1).date()
			try:
				div =  datetime.datetime.strptime(row[2], '%d %b %Y').date()
			except:
				div = datetime.datetime(1, 1, 1).date()
			husb = row[3]
			wife = row[5]
			children = row[7].split(" ")
			childbirth = {}
			count = 0
			with open('individuals.csv') as file2:
				file2.readline()
				birthH = None
				birthW = None
				
				for row2 in csv.reader(file2,delimiter=','):
					if husb in row2:	#Pretty sure alot of the user stories are basic if statements in here then we can make it a more generic method name
						birthH = row2[3]
						deathH = row2[4]
						if deathH != 'Alive':
							deathH = datetime.datetime.strptime(deathH, '%d %b %Y').date()
						if birthH != '??-??-????' or birthH != None:
							birthH = datetime.datetime.strptime(birthH, '%d %b %Y').date()
					if wife in row2:
						birthW =  row2[3]
						deathW =  row2[4]
						if deathW != "Alive":
							deathW = datetime.datetime.strptime(deathW, '%d %b %Y').date()
						if birthW != '??-??-????' or birthW != None:
							birthW = datetime.datetime.strptime(birthW, '%d %b %Y').date()
					#US13 less than 8 months apart or more than 2 days
					if len(children) > 1:
						for i in children:
							if i in row2:
								childbirth[i] = datetime.datetime.strptime(row2[3], '%d %b %Y').date()	
						
						temp = childbirth.copy()
						for key, value in childbirth.items():
							temp.pop(key)
							for key2, value2 in temp.items():
								if value > value2:
									a = value
									value = value2
									value2 = a
								if int(days_difference(value, value2, 'months')) <= 8 and int(days_difference(value, value2, 'days')) > 2 and count < len(children)-1:
									count += 1
									us13e = True
									print("ERROR: US13: " + key + "'s (" + str(value) + ") and " + key2 + "'s birthday(" + str(value2) + ") are either less than 8 months apart or more than 2 days apart")
					#US08/09
					if birthW != None and birthH != None:
						if len(children) > 0:
							for x in children: #x = childID
								if x in row2:
									if div > datetime.datetime(1, 1, 1).date():
										if int(days_difference(div,datetime.datetime.strptime(row2[3], '%d %b %Y').date(), 'months')) > 9:
											err.append('ERROR: US08: ' + x + "'s birthday(" + str(datetime.datetime.strptime(row2[3], '%d %b %Y').date()) + ") is more than 9 months after their parent's divorce(" + str(div) + ")")
									if married > datetime.datetime(1, 1, 1).date():
										if int(days_difference(datetime.datetime.strptime(row2[3], '%d %b %Y').date(), married, 'days')) > 0:
											err.append('ERROR: US08: ' + x + "'s birthday(" + str(datetime.datetime.strptime(row2[3], '%d %b %Y').date()) + ") is before their parent's marriage(" + str(married) + ")")
									if deathH != 'Alive':
										if int(days_difference(deathH, datetime.datetime.strptime(row2[3], '%d %b %Y').date(), 'months')) > 9:
											err.append('ERROR: US09: ' + x + "'s birthday(" + str(datetime.datetime.strptime(row2[3], '%d %b %Y').date()) + ") is more than 9 months after their father's death(" + str(deathW) + ")")
									if deathW != 'Alive':
										if int(days_difference(deathW, datetime.datetime.strptime(row2[3],'%d %b %Y').date(), 'days')) > 0:
											err.append('ERROR: US09: ' + x + "'s birthday(" + str(datetime.datetime.strptime(row2[3], '%d %b %Y').date()) + ") is after their mothers's death(" + str(deathW) + ")")
				US15(children, husb, wife)
					#US02/03 Birth after marriage, death before marriage
				if birthW != None and birthH != None:
					if married > datetime.datetime(1, 1, 1).date() and isinstance(married, datetime.date):	#to account for date=today for bad marriage dates
						if birthH > married:
							err.append("ERROR: US02: " + husb + "'s birth date (" + str(birthH) + ') is after his marriage date (' + str(married) + ')')
						if birthW > married:
							err.append("ERROR: US02: " + wife + "'s birth date (" + str(birthW) + ') is after her marriage date (' + str(married) + ')')
						if deathH != "Alive" and deathH < birthH:
							err.append("ERROR: US02: " + husb + "'s death(" + str(deathH) + ") is before his birth ( " + str(birthH) + ")")
						if deathW != "Alive" and deathW < birthW:
							err.append("ERROR: US02: " + wife + "'s death(" + str(deathW) + ") is before her birth ( " + str(birthW) + ")")
						if deathW != "Alive":
							if deathW < married:
								err.append("ERROR: US05: " + wife + "'s death date(" + str(deathW) + ") is before marriage date(" + str(married) + ")")
						if deathH != "Alive":
							if deathH < married:
								err.append("ERROR: US05: " + husb + "'s death date(" + str(deathH) + ") is before marriage date(" + str(married) + ")")
						#US 05/06  Marriage before death and divorce before death
					if div > datetime.datetime(1, 1, 1).date() and isinstance(div, datetime.date):
						if deathH != 'Alive':
							if deathH < div:
								err.append("ERROR: US06: " + husb + "'s death date(" + str(deathH) + ") is before divorce date(" + str(div) + ")")
						if deathW != 'Alive':
							if deathW < div:
								err.append("ERROR: US06: " + wife + "'s death date(" + str(deathW) + ") is before divorce date(" + str(div) + ")")
						#US01/04
					if div > datetime.datetime(1, 1, 1).date():
						if afterDate(div,today):
							err.append("ERROR: US01: " + husb + " and " + wife + "'s divorce date(" + str(div) + ") is after the current date(" + str(today) + ")")
					if married > datetime.datetime(1, 1, 1).date():
						if afterDate(married,today):
							err.append("ERROR: US01: " + husb + " and " + wife + "'s marriage date(" + str(div) + ") is after the current date(" + str(today) + ")")
					if married > datetime.datetime(1, 1, 1).date() and datetime.datetime(1, 1, 1).date() < div:
						if afterDate(married, div):
							err.append("ERROR: US04: " + husb + " and " + wife + "'s divorce date(" + str(div) + ") is before their marriage date(" + str(married) + ")")
					else:
						err.append("ERROR: GENERAL: Marriage or Divorce date for " + husb  + " and " + wife + " not available")
	return err

def INDI_ONLY():
	today = datetime.datetime.today().date()
	with open("individuals.csv", "r") as file:
		file.readline()
		for row in csv.reader(file, delimiter=','):
			bday = datetime.datetime.strptime(row[3], '%d %b %Y').date()
			dday = row[4]
			age = int(row[5])
			if dday != 'Alive':
				dday = datetime.datetime.strptime(dday, '%d %b %Y').date()
			
				US01(today, dday, bday, row[0])
				US03(dday, bday, age, row[0])
			US07(age, row[0])
	return 0
	
def US01(today, dday, bday, row):
	if today < dday:
		print('ERROR: US01: ' + row + "'s death(" + str(dday) + ") is after today(" + str(today) + ")")
		return False
	if today < bday:
		print('ERROR: US01: ' + row + "'s birth(" + str(bday) + ") is after today(" + str(today) + ")")
		return False
	return True
	
def US03(dday, bday, age, row):
		if bday > dday:
			print('ERROR: US03: ' + row + "'s death(" + str(dday) + ') is their before birth(' + str(bday) +')')
def US07(age, row):
	if age > 150 or age < 0:
		print('ERROR: US07: ' + row + "'s age(" + str(age) + ") is older than 150 or less than 0.")
		return False
	return True
	
def US10():
    f = open("families.csv", "r")
    fString = f.read()

    flist = []
    for line in fString.split("\n"):
        flist.append(line.split(","))

    i = open("individuals.csv", "r")
    iString = i.read()

    ilist = []
    for line in iString.split("\n"):
        ilist.append(line.split(","))

    rlist =[]
    for i in range(len(flist)-1):
        for j in range(len(ilist)-1):
            if flist[i][3] == ilist[j][0]:
                rlist.append("{},{},{}".format(ilist[j][0], ilist[j][3], flist[i][1]))

            if flist[i][5] == ilist[j][0]:
                rlist.append("{},{},{}".format(ilist[j][0], ilist[j][3], flist[i][1]))
    tlist = []
    for i in rlist:
        for line in i.split("\n"):
            tlist.append(line.split(","))

    for k in tlist:
        if (k[2] != 'Years not provided') & (k[1] != 'Years not provided') :
            mday = (datetime.datetime.strptime(k[2], '%d %b %Y')).date()
            bday = datetime.datetime.strptime(k[1], '%d %b %Y').date()
            nbday = bday + timedelta(days=14 * 365)

            if mday < nbday:
                print('ERROR: INDIVIDUAL: US10: ' + k[0] + ' Marriage on ' + k[2] + ' which is before 14 years of Birth which is ' + k[1])
def US14():
    i = open("individuals.csv", "r")
    iString = i.read()

    ilist = []
    for line in iString.split("\n"):
        ilist.append(line.split(","))
    count = 1
    people = []
    del ilist[0]
    for i in range(len(ilist) - 2):
        if (ilist[i][3] == ilist[i + 1][3]) & (ilist[i][6] == ilist[i + 1][6]):
            count += 1
            people.append('{}'.format(ilist[i][0]))

    if count > 5:
        print('ERROR: INDIVIDUAL: US14: Multiple Siblings are')
        for i in range(len(people)):
            print(people[i])
def US15(anArray, husb, wife):
	if(len(anArray) > 14):
		print("ERROR: US15: {} and {} have more than 15 children".format(husb, wife))
		return False
	return True
def US28():
    with open('families.csv','r+') as fp1:
        ret = True
        i = 1 
        for line in fp1.readlines():
            if i == 1:
                i += 1
                continue
            lineS = line.split(',')
            children = lineS[7].split()
            if len(children)==0 or len(children)==1:
                ret = False
                print("ERROR: FAMILY: US28: Family ",lineS[0],"has zero or one child")
            i+=1
    return ret
def US29():
     with open('individuals.csv','r+') as fp1:
        ret = True
        for line in fp1.readlines():
            lineS = line.split(',')
            if lineS[4] == 'Alive':
                print("ERROR: INDIVIDUAL: US30: Individual",lineS[0]," is not deceased")
                ret = False
     return ret