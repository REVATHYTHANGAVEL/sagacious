num = 16

#num = int(input("Enter a num: "))

if num < 0:
   print("Enter a positive num")
else:
   sum = 0
  
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)
