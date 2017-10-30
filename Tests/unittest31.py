import unittest
from datetime import datetime
import csv     
def US31_PassFile():
    with open("Passfile_US31.csv", "r+") as fp:
        ret=False
        for line in fp.readlines():
            lineS = line.split(",")
            if (lineS[4] == 'Alive') and ("None" in lineS[7]) and (int(lineS[5]) > 30):
                ret=True
                print ("INDIVIDUAL: US31:",lineS[0],"is alive who is above 30 years in age and never been married")
    return ret
def US31_FailFile():
    with open("Failfile_US31.csv", "r+") as fp:
        ret=False
        for line in fp.readlines():
            lineS = line.split(",")
            if (lineS[4] == 'Alive') and ("None" in lineS[7]) and (int(lineS[5]) > 30):
                ret=True
    return ret
class TestCase(unittest.TestCase):
    def test_US31_good(self):
        self.assertTrue(US31_PassFile())
    def test_US31_bad(self):
        self.assertFalse(US31_FailFile())
        

if __name__ == "__main__":   
    unittest.main()