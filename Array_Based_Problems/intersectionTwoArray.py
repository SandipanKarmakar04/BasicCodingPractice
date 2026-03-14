arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

intersection= []

for i in arr1:
    if i in arr2:
        intersection.append(i)

print(intersection)
            