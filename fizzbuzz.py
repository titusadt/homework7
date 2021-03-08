

def buzz_check(num):
   output = []
   for i in range (1, num+1):
      if i % 3 == 0:
	      output.append('Fizz')
      elif i % 5 ==0:
	      output.append('Buzz')
      elif i % 3 ==0 and i % 5 ==0:
	      output.append('FizzBuzz')
      else:
	      output.append(str(i))
   return output

def main():
   print('\n'.join(buzz_check(100)))

main()

