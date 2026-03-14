li = [25, 16,38,10,35,48,20,50]

if (li[0]>li[1]):
    max1 = li[0]
    max2 = li[1]
else:
    max1 = li[1]
    max2 = li[0]

for i in range(2, len(li)):
    if (li[i]>max1):
        max2=max1
        max1=li[i]
    elif (li[i]>max2):
        max2=li[i]

print(max2)