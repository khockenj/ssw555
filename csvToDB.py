import pymysql

# Creating database for Families

# Opening CSV File
f = open("families.csv", "r")
fString = f.read()

flist = []
for line in fString.split("\n"):
    flist.append(line.split(","))
# connect to DB

hostname = 'localhost'
username = 'root'
password = 'vardaan'
database = 'Agile'

db = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
cursor = db.cursor()

# Drop table if it already exists
cursor.execute("DROP TABLE IF EXISTS FAMILIES")

# Create table from first line in fList
FID = flist[0][0]
Married = flist[0][1]
Divorced = flist[0][2]
HusbandID = flist[0][3]
HusbandName = flist[0][4]
WIfeID = flist[0][5]
WifeName = flist[0][6]
Children = flist[0][7]

# Create FAMILIES table //place comma after each column except last one

queryCreateFamilyTable = """CREATE TABLE FAMILIES(
                            FID VARCHAR(255) ,
                            Married DATE ,
                            Divorced DATE ,
                            HusbandID VARCHAR(255) ,
                            HusbandName VARCHAR(255) ,
                            WifeID VARCHAR(255) ,
                            WifeName VARCHAR(255) ,
                            Children VARCHAR(255) )"""

cursor.execute(queryCreateFamilyTable)

# Delete first row beacuse it is not needed
del flist[0]

# Inserting values to the table FAMILIES
rows = ''
for i in range(len(flist) - 1):
    rows += "('{}', '{}', '{}', '{}', '{}', '{}','{}' )".format(flist[i][0], flist[i][1], flist[i][2], flist[i][3],
                                                                flist[i][4], flist[i][5], flist[i][6], flist[i][7])
    if i != len(flist) - 2:
        rows += ','

queryInsertFamily = "INSERT INTO FAMILIES VALUES" + rows + ";"

try:
    # Execute the Query
    cursor.execute(queryInsertFamily)
    db.commit()
except:
    # Rollback if any error
    db.rollback()
db.close()

# Creating database for Individuals

# Opening CSV File
f = open("individuals.csv", "r")
fString = f.read()

flist = []
for line in fString.split("\n"):
    flist.append(line.split(","))
# connect to DB

hostname = 'localhost'
username = 'root'
password = 'vardaan'
database = 'Agile'

db = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
cursor = db.cursor()

# Drop table if it already exists
cursor.execute("DROP TABLE IF EXISTS INDIVIDUALS")

# Create table from first line in fList
ID = flist[0][0]
NAME = flist[0][1]
GENDER = flist[0][2]
BIRTHDAY = flist[0][3]
DEATH = flist[0][4]
AGE = flist[0][5]
CHILDIN = flist[0][6]
SPOUSEIN = flist[0][7]

# Create FAMILIES table //place comma after each column except last one

queryCreateIndiTable = """CREATE TABLE INDIVIDUALS(
                            ID VARCHAR(255) ,
                            NAME VARCHAR(255) ,
                            GENDER VARCHAR(255) ,
                            BIRTHDAY DATE ,
                            DEATH DATE ,
                            AGE INT(25) ,
                            CHILDIN VARCHAR(255) ,
                            SPOUSEIN VARCHAR(255) )"""

cursor.execute(queryCreateIndiTable)

# Delete first row beacuse it is not needed
del flist[0]

# Inserting values to the table FAMILIES
rows = ''
for i in range(len(flist) - 1):
    rows += "('{}', '{}', '{}', '{}', '{}', '{}','{}' )".format(flist[i][0], flist[i][1], flist[i][2], flist[i][3],
                                                                flist[i][4], flist[i][5], flist[i][6], flist[i][7])
    if i != len(flist) - 2:
        rows += ','

queryInsertIndi = "INSERT INTO INDIVIDUALS VALUES" + rows + ";"

try:
    # Execute the Query
    cursor.execute(queryInsertIndi)
    db.commit()
except:
    # Rollback if any error
    db.rollback()
db.close()
