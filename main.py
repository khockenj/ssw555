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
meths.INDI_ONLY()
meths.INDI_FAM_relations()
meths.US10()
meths.US14()
meths.US28()
meths.US29()