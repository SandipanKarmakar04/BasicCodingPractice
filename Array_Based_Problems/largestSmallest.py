ar = [10, 25, 5, 40, 15]

large = ar[0]
small = ar[0]

for i in ar:
    if i >= large:
        large = i
    if i <= small:
        small = i

print("large element:", large)
print("small element:", small)