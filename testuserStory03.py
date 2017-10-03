from unittest import Testcase

class test_birth_before_death(TestCase):
    def test_birth_before_death1(self):

        individuals, _ = GEDCOMParser(acceptfile)
        self.assertTrue(birth_before_death(individuals))

    def test_birth_before_death2(self):

        individuals, _ = GEDCOMParser(acceptfile)
        self.assertEqual(birth_before_death(individuals),True)

    def test_birth_before_death3(self):

        individuals, _ = GEDCOMParser(acceptfile)
        self.assertIsNot(birth_before_death(individuals),False)

    def test_birth_before_death4(self):

        individuals, _ = GEDCOMParser(fail_file1)
        self.assertIsNotNone(birth_before_death(individuals))

    def test_birth_before_death5(self):
        individuals, _ = GEDCOMParser(acceptfile)
        self.assertIs(birth_before_death(individuals),True)
