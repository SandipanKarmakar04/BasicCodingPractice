def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)


n=int(input("Enter the number of terms you want: "))

for i in range(n):
    print(fibonacci(i), end=", ")