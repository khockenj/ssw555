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
	#birth before death
	with open('families.csv') as file1:
		file1.readline()
		for row in csv.reader(file1, delimiter=','):
			married = row[1]
			husb = row[3]
			wife = row[5]
			with open('individuals.csv') as file2:
				file2.readline()
				birthH = '??-??-????'
				birthW = '??-??-????'
				for row2 in csv.reader(file2,delimiter=','):
					if husb in row2:	#Pretty sure alot of the user stories are basic if statements in here then we can make it a more generic method name
						birthH = row2[3]
						deathH = row2[5]
					if wife in row2:
						birthW = row2[3]
						deathW = row2[5]
			if birthH > married:
				err.append(husb + "'ss birthday (" + birthH + ') is before his marriage date (' + married + ')')
			if birthW > married:
				err.append(wife + "'s birthday (" + birthW + ') is before her marriage date (' + married + ')')	
			if deathH != "Alive" and deathH < birthH:
				err.append(husb + "'s death(" + deathH + ")is before his birth ( " + birthH + ")")
			if deathW != "Alive" and deathW < birthW:
				err.append(wife + "'s death(" + deathW + ")is before his birth ( " + birthW + ")")
	return err
					
		
