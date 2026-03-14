# Example:
# 121 if reversed still it form 121, so palindrome.
# 568 if reversed it will form 865, so not palindrome.

no = int(input("Enter the number to check palindrome: "))
temp = no
sm = 0

while no > 0:
    rem = no%10
    sm = sm*10+rem
    no = no//10

if temp == sm:
    print("Palindrome")
else:
    print("Not Palindrome")