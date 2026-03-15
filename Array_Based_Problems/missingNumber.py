# arr = [1, 2, 4, 5, 7]

# n = len(arr) + 1

# total = n * (n+1) // 2
# miss = total - sum(arr)

# print(miss)

# Another Method
arr = [1,2,4,5,7]

n = max(arr)

for i in range(1, n+1):
    if i not in arr:
        print(i)