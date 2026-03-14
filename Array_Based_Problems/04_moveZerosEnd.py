ar = [0,1,0,3,12]
result= []
count = 0
for i in ar:
	if i != 0:
		result.append(i)
	else:
		count += 1

for j in range(count):
	result.append(0)

print(result)
