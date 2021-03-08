

def check_year(prompt):
   if prompt % 4 == 0 and prompt % 100 != 0:
      print(prompt, "is a leap year")
   elif prompt % 400 == 0:
      print(prompt, "is a Leap Year")
   elif prompt % 100 == 0:
      print(prompt, "is not a Leap Year")
   else:
      print(prompt, "is not a Leap Year")
