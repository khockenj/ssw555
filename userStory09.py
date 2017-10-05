from datetime import datetime, timedelta
import csv


def birth_before_parents_died():
    with open("families.csv", "r+") as fp:
        family_id = []
        indi_id = []
        father_id = []
        mother_id = []


        for line in fp.readlines():
            lineS = line.split(',')
            family_id.append(lineS[0])
            indi_id.append(lineS[7])
            father_id.append(lineS[3])
            mother_id.append(lineS[5])

    family_id = family_id[1:]
    indi_id = indi_id[1:]
    father_id = indi_id[1:]
    mother_id = indi_id[1:]

    family_to_indv = dict(zip(family_id, indi_id))
    family_to_father_id = dict(zip(family_id, father_id))
    family_to_mother_id = dict(zip(family_id, mother_id))


    id_to_birthdates_child = {}

    with open('individuals.csv','r+') as fp1:
        for line in fp1.readlines():
            lineS = line.split(',')
            for i in family_to_indv.values():
                if lineS[0] in i:
                    id_to_birthdates_child[lineS[0]]= lineS[3]

    id_to_deathdates_father = {}

    with open('individuals.csv', 'r+') as fp1:
        for line in fp1.readlines():
            lineS = line.split(',')
            for i in family_to_father_id.values():
                if lineS[0] in i:
                    id_to_deathdates_father[lineS[0]] = lineS[4]

    id_to_deathdates_mother = {}

    with open('individuals.csv', 'r+') as fp1:
        for line in fp1.readlines():
            lineS = line.split(',')
            for i in family_to_mother_id.values():
                if lineS[0] in i:
                    id_to_deathdates_mother[lineS[0]] = lineS[4]

    fddate = []
    mddate =[]
    mddate = []


    for k,v in family_to_indv.items():
        if family_to_mother_id.get(k) != 'NA':
            for l,m in id_to_deathdates_mother.items():
                if l in v:
                    mddate.append(m)

    mom_death = dict(zip(family_id, mddate))

    for k,v in family_to_indv.items():
        if family_to_mother_id.get(k) != 'NA':
            for l,m in id_to_deathdates_father.items():
                if l in v:
                    fddate.append(m)

    dad_death = dict(zip(family_id, mddate))

    flag1 = 0
    flag2 = 0
    for k,v in family_to_indv.items():
        if mom_death.get(k) != 'NA':
            for l,m in id_to_birthdates_child.items():
                if l in v:
                    bday = m
                    mardate = mom_death.get(k)
                    if(datetime.strptime(bday, '%d-%b-%y') > datetime.strptime(mardate, '%d-%b-%y')) :
                            flag1 = 1


    for k,v in family_to_indv.items():
        if dad_death.get(k) != 'NA':
            for l,m in id_to_birthdates_child.items():
                if l in v:
                    bday2 = m
                    mardate2 = dad_death.get(k)
                    if(datetime.strptime(bday, '%d-%b-%y') > (datetime.strptime(mardate2, '%d-%b-%y') + timedelta(days=270))):
                            flag2 = 1

    if flag1==1 & flag2==1:
        print('ERROR: INDIVIDUAL: US09: Child Birth Before parents died')


