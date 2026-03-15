arr = [1,2,3,4,5]
k = 2

# Left Rotation:
rotated = arr[k:] + arr[:k]
print(rotated)

# Right Rotation:
n = len(arr)
rotated = arr[n-k:] + arr[:n-k]
print(rotated)