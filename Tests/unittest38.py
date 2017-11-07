import unittest
from datetime import datetime,date
import csv     
def US38_PassFile():
    with open("Passfile_US38.csv", "r+") as fp:
        ret=False
        i = 0
        for line in fp.readlines():
            if (i == 0):
                i += 1
                continue
            lineS = line.split(",")
            today = date.today()
            today = datetime(today.year, today.month, today.day)
            today.strftime('%d-%b-%y')
            diff =  today - (datetime.strptime(lineS[3], '%d-%b-%y'))
            diff = int(str(diff).split()[0])
            if(-30<diff and diff<0):
                ret=True
                print ("INDIVIDUAL: US38:",lineS[0],"has an upcoming birthday in the next 30 days")
            i += 1
    return ret
def US38_FailFile():
    with open("Failfile_US38.csv", "r+") as fp:
        ret=True
        i = 0
        for line in fp.readlines():
            if (i == 0):
                i += 1
                continue
            lineS = line.split(",")
            today = date.today()
            today = datetime(today.year, today.month, today.day)
            today.strftime('%d-%b-%y')
            diff =  today - (datetime.strptime(lineS[3], '%d-%b-%y'))
            diff = int(str(diff).split()[0])
            if(-30<diff and diff<0):
                ret=False
            i += 1
    return ret
class TestCase(unittest.TestCase):
    def test_US38_good(self):
        self.assertTrue(US38_PassFile())
    def test_US38_bad(self):
        self.assertFalse(US38_FailFile())
        

if __name__ == "__main__":   
    unittest.main()
