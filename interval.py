lower=int(input("Enter lower limit for the range:"))
upper=int(input("Enter upper limit for the range:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
