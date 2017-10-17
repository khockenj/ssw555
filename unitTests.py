import unittest
from methods import US15

class TestCases(unittest.TestCase):

#Tests for US15 (Fewer than 15 siblings): There should be fewer than 15 siblings in a family
    def test_US15_lessthan15(self):
        array = [1,2,3]
        husb = "Ahusband"
        wife = "Awife"
        self.assertTrue(US15(array, husb, wife))

    def test_US15_exactly15(self):
        array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        husb = "Ahusband"
        wife = "Awife"
        self.assertFalse(US15(array, husb, wife))

    def test_US15_morethan15(self):
        array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        husb = "Ahusband"
        wife = "Awife"
        self.assertFalse(US15(array, husb, wife))

if __name__ == '__main__':
    unittest.main()
