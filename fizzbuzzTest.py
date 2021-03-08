import unittest
import fizzbuzz


class TestCase(unittest.TestCase):
   def test1(self):
      self.assertEqual(fizzbuzz.buzz_check(18), "Fizz");


   def test1(self):
      self.assertEqual(fizzbuzz.buzz_check(25), "Buzz");

   def test1(self):
      self.assertEqual(fizzbuzz.buzz_check(30), "FizzBuzz");

   
if __name__ == '__main__':
   unittest.main()
