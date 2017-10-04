#So, put all of your methods in this file, and if you want to call them in the gedcom2csv call it as meths.METHODNAME
from datetime import datetime
import csv
def afterCurrentDate(aDate):
	if aDate > datetime.today().date():
		return True #invalid date
	else:
		return False
		
def days_difference(d1, d2):
	if afterCurrentDate(d1): 
		return 0
	else:
		return (d2-d1).days
    
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

