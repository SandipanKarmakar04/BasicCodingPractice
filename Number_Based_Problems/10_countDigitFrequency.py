n = input("Enter the number")

freq = {}

for digit in n:
    freq[digit] = freq.get(digit, 0)+1

print(freq)

print("the frequency is: ")
for key in freq:
    print(key, freq[key])

ck = input("Check for specific number's frequency: ")
print("Frequency is: ", freq[ck])