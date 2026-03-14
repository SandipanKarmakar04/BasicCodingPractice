no = int(input("Enter the number to check palindrome: "))
temp = no
sm = 0

while no > 0:
    rem = no%10
    print(rem, end="")
    no = no//10