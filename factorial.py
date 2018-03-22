num = 7
factorial = 1
if num < 0:
   print("Sorry, If the factorial does not exist for negative numbers")
elif num == 0:
   print("If The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
