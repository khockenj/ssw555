#So, put all of your methods in this file, and if you want to call them in the gedcom2csv call it as meths.METHODNAME
from datetime import datetime

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