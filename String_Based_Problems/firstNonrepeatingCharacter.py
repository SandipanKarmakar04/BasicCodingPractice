
# This technique is correct but slow:
# s = input()

# for i in s:
# 	if s.count(i) == 1:
# 		print(i)
# 		break


s = input()

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0)+1

for ch in s:
    if freq[ch] == 1:
        print("Non repeat character: ", ch)
        break