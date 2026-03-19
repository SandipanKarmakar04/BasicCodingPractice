# no = 1634
# 1^4 + 6^4 + 3^4 + 4^4 = 1234 the same number came, Armstrong number
# --------------------------------------------------
# no = 163
# 1^3 + 6^3 + 3^3 = 1378 the same number not came, not an Armstrong number

no=int(input("Enter the number to check armstrong or not: "))
t1 = no

rem = 0

arm = 0

#check for the length of the input
ln = len(str(t1))

while t1!=0:
    rem=t1%10
    mul = 1
    for i in range (ln):
        mul=mul*rem
    arm=arm+mul
    t1=t1//10

print(arm)

if arm == no:
    print("Armstrong")
else:
    print("Not Armstrong")