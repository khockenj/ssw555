from datetime import datetime


def birth_before_death_of_parents(gedcom_file):
    
    r = {"passed": [], "failed": []}

    for fam in gedcom_file.families:
        for child in (c for c in fam.children if c.has("birth_date")):
            chk_mom = fam.has("wife") and fam.wife.has("death_date")
            chk_dad = fam.has("husband") and fam.husband.has("death_date")
            mom_pass = child.birth_date < fam.wife.birth_date if chk_mom else None
            dad_pass = ((fam.husband.birth_date.dt - child.birth_date.dt).days / 30) > 9 if chk_dad else None
            msg = "{0} has Child {1} with birth date {2} and has".format(fam, child, child.birth_date)

            if mom_pass is None:
                msg += " mother {0} with no death date".format(fam.wife)
            else:
                msg += " mother {0} with death date {1}".format(fam.wife, fam.wife.death_date)

            if dad_pass is None:
                msg += " and father {0} with no death date.".format(fam.husband)
            else:
                msg += " and father {0} with death date {1}.".format(fam.husband, fam.husband.death_date)

            passed = ((mom_pass is None) or (mom_pass is True)) and ((dad_pass is None) or (dad_pass is True))
            status = "passed" if passed else "failed"
            r[status].append({"message": msg})

    return r
