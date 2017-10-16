from prettytable import from_csv 
import methods as meths
import gedcom2csv

readTable = open("individuals.csv", "r") 
table = from_csv(readTable)
readTable.close()
print("Individuals")
print(table)
print("Families")
readTable = open("families.csv", "r") 
table = from_csv(readTable)
readTable.close()
print(table)
errors = meths.INDI_ONLY()
for err in errors:
	print(err)
errors2 = meths.INDI_FAM_relations()
for err in errors2:
	print(err)
	
meths.US10()
meths.US14()
