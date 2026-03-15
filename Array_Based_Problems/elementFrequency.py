ar = [2, 1, 3, 4, 2, 4, 5, 4]

freq = {}

for i in ar:
    freq[i] = freq.get(i, 0)+1

print(freq)