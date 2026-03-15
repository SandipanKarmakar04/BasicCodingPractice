arr = [2, 7, 11, 15, -2]
target = 9

for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		val = arr[i]+arr[j]
		if val == target:
			print(arr[i],"+",arr[j],": 9")
