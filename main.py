from prettytable import from_csv 
import gedcom2csv
import methods as meths
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