# Example:
# 6 --> 1, 2, 3 only can divide the number 6.
# Sum of all these divisors is also 6 (1+2+3 = 6), so it is a perfect number.

no = int(input())
sm=0
for i in range (1, no):
	if no % i == 0:
		sm += i
if sm == no:
	print("perfect number")
else:
	print("Not a perfect number")
