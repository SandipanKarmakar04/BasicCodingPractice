start = int(input("Enter the start no.: "))
stop = int(input("Enter the stop no.: "))


for i in range (start, stop+1):

    if i < 2:
        print(i, "not valid")
        continue

    for j in range(2, i):
        if i%j == 0:
            print(i, "not prime")
            break
    else:
        print(i, "prime")