import unittest
from datetime import datetime,date
import csv     
def US36_PassFile():
    with open("Passfile_US36.csv", "r+") as fp:
        ret=False
        i = 0
        for line in fp.readlines():
            if (i == 0):
                i += 1
                continue
            lineS = line.split(",")
            if (lineS[4]!='Alive'):
             today = date.today()
             today = datetime(today.year, today.month, today.day)
             today.strftime('%d-%b-%y')
             diff =  today - (datetime.strptime(lineS[4], '%d-%b-%y'))
             diff = int(str(diff).split()[0])
             if(0<diff and diff<30):
                 ret=True
                 print ("INDIVIDUAL: US36:",lineS[0],"has died in the last 30 days")
             i += 1
    return ret
def US36_FailFile():
    with open("Failfile_US36.csv", "r+") as fp:
        ret=True
        i = 0
        for line in fp.readlines():
            if (i == 0):
                i += 1
                continue
            lineS = line.split(",")
            if (lineS[4]!='Alive'):
             today = date.today()
             today = datetime(today.year, today.month, today.day)
             today.strftime('%d-%b-%y')
             diff =  today - (datetime.strptime(lineS[4], '%d-%b-%y'))
             diff = int(str(diff).split()[0])
             if(0<diff and diff<30):
                 ret=False
             i += 1
    return ret
class TestCase(unittest.TestCase):
    def test_US36_good(self):
        self.assertTrue(US36_PassFile())
    def test_US36_bad(self):
        self.assertFalse(US36_FailFile())
        

if __name__ == "__main__":   
    unittest.main()
