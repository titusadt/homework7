import unittest
import leap_year

class TestCase(unittest.TestCase):
   def test1(self):
      self.assertEqual(leap_year.check_year(2016), "Leap Year")

   def test2(self):
      self.assertEqual(leap_year.check_year(2017), "not Leap Year")


if __name__ == '__main__':
   unittest.main()
