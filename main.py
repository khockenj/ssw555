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
meths.US_03()
meths.US_08()
meths.marriage_before_divorce()
meths.birth_before_parents_died()
birthb4 = meths.birthBeforeMarriage()
for err in birthb4:
	print(err)