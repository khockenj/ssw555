def birth_before_marriage_of_parents(gedcom_file):
    
    r = {"passed": [], "failed": []}
    div_msg = "{0} with marriage date {1} and divorce date {2} has a child {3} born {4}"
    mar_msg = "{0} with marriage date {1} has a child {2} born {3}"
    for fam in (f for f in gedcom_file.families if f.has("marriage_date")):

        if not fam.has("marriage_date"):
            continue  # Project Overview Assumptions not met
        if not fam.has("husband") or not fam.husband.has("birth_date"):
            continue  # Project Overview Assumptions not met
        if not fam.has("wife") or not fam.wife.has("birth_date"):
            continue  # Project Overview Assumptions not met

        for child in (c for c in fam.children if c.has("birth_date")):
            out = {}
            passed = fam.marriage_date < child.birth_date
            if fam.divorce_date:
                out["message"] = div_msg.format(fam, fam.marriage_date, fam.divorce_date, child, child.birth_date)
                passed = passed and (fam.divorce_date > child.birth_date)
            else:
                out["message"] = mar_msg.format(fam, fam.marriage_date, child, child.birth_date)
            r["passed"].append(out) if passed else r["failed"].append(out)

    return r
