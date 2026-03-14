no = int(input("Enter the number to check perfect square: "))

i = 1
flag = False

while i*i <= no:
    if i*i == no:
        flag = True
        break
    i += 1

if flag:
    print("Perfect Square")
else:
    print("Not A perfect Square")