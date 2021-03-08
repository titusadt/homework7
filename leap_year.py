

def check_year(prompt):
   if prompt % 4 == 0 and prompt % 100 != 0:
      return "Leap Year"
   elif prompt % 400 == 0:
      return "Leap Year"
   elif prompt % 100 == 0:
      return "not Leap Year"
   else:
      return "not Leap Year"
