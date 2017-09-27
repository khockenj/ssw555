#Import GEDCOM into CSV
import csv
with open('projectGED.ged', 'r') as in_file:
	with open('individuals', 'w', newline='') as out_file:
		writer = csv.writer(out_file)
		death = 'Alive'
		counter = 0
		writer.writerow(('ID', 'Name', 'Gender', 'Birthday', 'Death', 'Child in', 'Spouse in'))
		for line in in_file:
			lineS = line.split(" ")
			
			if lineS[0].strip() == '1' and lineS[1].strip() not in ['SOUR', 'FILE', 'DEST', 'GEDC', 'SUBM', 'SUBN', 'CHAR']:
				if lineS[1].strip() == 'NAME':
					name = lineS[2].strip() + " " + lineS[3].strip()
				elif lineS[1].strip() == 'SEX':
					sex = lineS[2].strip()
				elif lineS[1].strip() == 'BIRT':
					birth = " ".join(next(in_file).split(" ")[2:5]).strip()
				elif lineS[1].strip() == 'DEAT':
					death = " ".join(next(in_file).split(" ")[2:5]).strip()
				elif lineS[1].strip() == 'FAMS':
					fams = lineS[2].strip()
				elif lineS[1].strip() == 'FAMC':
					famc = lineS[2].strip()
			elif lineS[0].strip() == '0' and lineS[1].strip() not in ['NOTE', 'HEAD', 'TRLR']:
				if counter != 0 and lineS[2].strip() != 'FAM':
					writer.writerow((id,name,sex,birth,death,famc,fams))
				counter += 1
				if lineS[2].strip() == 'INDI':
					id = lineS[1].strip()
		writer.writerow((id,name,sex,birth,death,famc,fams))
in_file.close()
with open('projectGED.ged', 'r') as in_file:	
	with open('families.csv', 'w', newline='') as out_file:
		writer = csv.writer(out_file)
		writer.writerow(('FID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'))
		child = []
		divorce = 'Years not provided'
		hname = 'Joey'
		wname = 'Joeyina'
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