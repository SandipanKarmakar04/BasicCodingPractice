no = int(input("Enter the number to check summation value: "))

temp = no
sm = 0
while temp > 0:
    digits = temp % 10
    sm += digits
    temp = temp // 10

print(sm)