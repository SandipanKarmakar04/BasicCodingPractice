n = int(input("Enter a number to check prime or not: "))

if n < 2:
    print("Enter a number more than 2")
else:
    for i in range (2, n):
        if n%i == 0:
            print("The no. is not prime.")
            break
    else:
        print("The no. is prime.")