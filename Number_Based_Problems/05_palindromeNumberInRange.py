st = int(input("Start value: "))
sp = int(input("Stop value: "))

for i in range(st, sp+1):
    temp = i
    result = 0
    while temp > 0:
        rem = temp % 10
        result = result*10+rem  #this will multiply with the number, so that the length figure came.
        temp = temp // 10
    if i == result:
        print(i, "Palindrome")
    else:
        print(i, "Not palindrome")