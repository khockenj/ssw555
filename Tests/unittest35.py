import unittest
from datetime import datetime,date
import csv     
def US35_PassFile():
    with open("Passfile_US35.csv", "r+") as fp:
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
            #print (today)
            #print(datetime.strptime(lineS[3], '%d-%b-%y'))
            diff =  today - (datetime.strptime(lineS[3], '%d-%b-%y'))
            diff = int(str(diff).split()[0])
            #print (diff)
            if(0<diff and diff< 30):
                ret=True
                print ("INDIVIDUAL: US35:",lineS[0],"was born in the last 30 days")
            i += 1
    return ret
def US35_FailFile():
    with open("Passfile_US35.csv", "r+") as fp:
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
            if(0<diff and diff< 30):
                ret=False
            i += 1
    return ret
class TestCase(unittest.TestCase):
    def test_US35_good(self):
        self.assertTrue(US35_PassFile())
    def test_US35_bad(self):
        self.assertFalse(US35_FailFile())
        

if __name__ == "__main__":   
    unittest.main()
