st = input("Entre the string: ")

result = ""

for i in st:
    if i.isalnum() or i==" ":
        result += i

print(result)