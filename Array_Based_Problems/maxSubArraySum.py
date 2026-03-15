ar = [-2,1,-3,4,-1,2,1,-5,4]
mxsm=0
for i in range (len(ar)):
	sm = 0
	for j in range(i,len(ar)):
		sm += ar[j]
		if sm > mxsm:
			mxsm = sm
print(mxsm) 
