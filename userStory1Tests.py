import unittest
import datetime
from userStory1 import afterCurrentDate

class TestCases(unittest.TestCase):

    def test_avaliddate(self):
        self.assertEqual(afterCurrentDate(datetime.datetime(1960,1,17)), None)

    def test_today(self):
        self.assertEqual(afterCurrentDate(datetime.datetime.today()), None)

    def test_wrongyear(self):
        self.assertEqual(afterCurrentDate(datetime.datetime.today() + datetime.timedelta(days=365)), 1)

    def test_wrongday(self):
        self.assertEqual(afterCurrentDate(datetime.datetime.today() + datetime.timedelta(days=1)), 1)

    def test_wrongmonth(self):
        self.assertEqual(afterCurrentDate(datetime.datetime.today() + datetime.timedelta(days=31)), 1)

if __name__ == '__main__':
    unittest.main()
