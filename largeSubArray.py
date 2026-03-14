ar = [1,0,0,1,0,1,1]

for c in range(len(ar)):
    if ar[c] == 0:
        ar[c] = -1
print (ar)

count0 = 0
count1 = 0

for i in ar:
    for j in ar:
        