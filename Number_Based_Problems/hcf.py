a=int(input())
b=int(input())

h=0
if a<b:
    h=a
else:
    h=b

while h>=1:
    if (a%h==0 and b%h==0):
        break
    h -= 1
print("hcf is: ", h)