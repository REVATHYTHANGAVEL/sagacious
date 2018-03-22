def check(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("If the Number not prime")
            return False
        else:
            return check(n, div-1)
    else:
        print("If the Number is prime")
        return 'True'
n=int(input("Enter the number: "))
check(n)
