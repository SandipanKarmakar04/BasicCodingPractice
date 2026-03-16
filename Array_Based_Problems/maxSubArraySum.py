ar = [1,2,3,8,-3]
mxsm=0
for i in range (len(ar)):
	sm = 0
	for j in range(i,len(ar)):
		sm += ar[j]
		if sm > mxsm:
			mxsm = sm
print(mxsm) 
