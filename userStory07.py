from datetime import datetime


def less_then_150_years_old(gedcom_file):
    """ Death should be less than 150 years after birth for dead people, and
        current date should be less than 150 years after birth for all living people
    :sprint: 2
    :author: Constantine Davantzis
    :param gedcom_file: GEDCOM File to check
    :type gedcom_file: parser.File
    """
    r = {"passed": [], "failed": []}
    msg = {"death": "Individual {0} was born {1} and died {2} years later on {3}".format,
           "alive": "Individual {0} was born {1} and is {2} years old as of {3} (current date)".format}

    for indi in gedcom_file.individuals:
        if not indi.has("birth_date"):
            continue  # Project Overview Assumptions not met
        out = {}
        if indi.has("death_date"):
            out["message"] = msg["death"](indi, indi.birth_date, indi.age, indi.death_date)
        else:
            out["message"] = msg["alive"](indi, indi.birth_date, indi.age, NOW_STRING)
        r["passed"].append(out) if indi.age < 150 else r["failed"].append(out)

    return r
