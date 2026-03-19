li = list(map(int, input().split()))
li.sort()

val = int(input())

low = 0
high = len(li)-1

while low <= high:
    mid = (low + high) // 2
    if li[mid] == val:
        print("found")
        break
    if (val> li[mid]):
        low = mid + 1
    else:
        high = mid - 1
else:
    print("not found")