arr = [10, 25, 5, 40, 15]

even = 0
odd = 0

print("Even numbers:")
for i in arr:
    if i % 2 == 0:
        print(i)
        even += 1

print("Odd numbers:")
for i in arr:
    if i % 2 != 0:
        print(i)
        odd += 1

print("Even count:", even)
print("Odd count:", odd)