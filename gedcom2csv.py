#Import GEDCOM into CSV
import csv
from datetime import datetime, date
import methods as meths

with open('testGED.ged', 'r') as in_file:
	with open('individuals.csv', 'w', newline='') as out_file:
		writer = csv.writer(out_file)
		counter = 0
		#Defaults for GEDCOMS that are missing things
		name = "Name"
		sex = "Sex"
		birth = "Birth"
		death = "Alive"
		fams = "Fams"
		famc = "famc"
		age = "Age"
		writer.writerow(('ID', 'Name', 'Gender', 'Birthday', 'Death', 'Age', 'Child in', 'Spouse in'))
		for line in in_file:
			lineS = line.split(" ")
			
			if lineS[0].strip() == '1' and lineS[1].strip() not in ['SOUR', 'FILE', 'DEST', 'GEDC', 'SUBM', 'SUBN', 'CHAR']:
				if lineS[1].strip() == 'NAME':
					name = lineS[2].strip() + " " + lineS[3].strip()
				elif lineS[1].strip() == 'SEX':
					sex = lineS[2].strip()
				elif lineS[1].strip() == 'BIRT':
					birth = " ".join(next(in_file).split(" ")[2:5]).strip()
					birthD = datetime.strptime(birth, '%d %b %Y').date()
					today = datetime.today().date()
					age = int((meths.days_difference(birthD, today))/365)
					if(age > 150 or age < 0):
						age = "INVALID AGE"
				elif lineS[1].strip() == 'DEAT':
					death = " ".join(next(in_file).split(" ")[2:5]).strip()
				elif lineS[1].strip() == 'FAMS':
					fams = lineS[2].strip()
				elif lineS[1].strip() == 'FAMC':
					famc = lineS[2].strip()
			elif lineS[0].strip() == '0' and lineS[1].strip() not in ['NOTE', 'HEAD', 'TRLR']:
				if counter != 0 and lineS[2].strip() != 'FAM':
					writer.writerow((id,name,sex,birth,death,age,famc,fams))
				counter += 1
				if lineS[2].strip() == 'INDI':
					id = lineS[1].strip()
		writer.writerow((id,name,sex,birth,death,age,famc,fams))
in_file.close()
with open('projectGED.ged', 'r') as in_file:	
	with open('families.csv', 'w', newline='') as out_file:
		writer = csv.writer(out_file)
		writer.writerow(('FID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'))
		child = []
		divorce = 'Years not provided'
		married = 'Years not provided'
		counter = 0
		for line in in_file:
			lineS = line.split(" ")
			if lineS[0].strip() == '1' and lineS[1].strip() in ['HUSB', 'CHIL', 'WIFE']:
				if lineS[1].strip() == 'HUSB':
					husb = lineS[2].strip()
				elif lineS[1].strip() == 'WIFE':
					wife = lineS[2].strip()
				elif lineS[1].strip() == 'CHIL':
					child.append(lineS[2].strip())
			elif lineS[0].strip() == '0' and lineS[1].strip() not in ['NOTE', 'HEAD', 'TRLR']:
				if lineS[2].strip() == 'FAM' and counter != 0:
					with open('projectGED.ged', 'r') as in_file2:
						for line2 in in_file2:
							if husb in line2.split(" "):
								hname = " ".join(next(in_file2).split(" ")[2:4]).strip()
							elif wife in line2.split(" "):
								wname = " ".join(next(in_file2).split(" ")[2:4]).strip()
					in_file2.close()
					writer.writerow((fid,married,divorce,husb,hname,wife,wname," ".join(child)))
				if lineS[2].strip() != 'INDI':
					fid = lineS[1].strip()
					child = []
					counter += 1
in_file.close()
print('GEDCOM converted to .csv')