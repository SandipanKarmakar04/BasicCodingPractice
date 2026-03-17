s = input()

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0)+1

maxChar= max(freq, key=freq.get)

print(maxChar)
