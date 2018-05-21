a=int(input())
if(a%2==0):
    if(a in range (2,6)):
        print('not weird')
    elif(a in range(6,21)):
       print('weird')
    elif(a>20):
       print('not wried')
else:
   print('odd')
