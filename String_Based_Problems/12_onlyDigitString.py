# st = input("Entre the string: ")

# result = ""

# for i in st:
#     if i.isdigit():
#         result += i

# print(result)


st = input("Entre the string: ")

flag=True

for i in st:
    if i.isalpha():
        flag = False
        break

if flag == False:
    print("Mixed string")
else:
    print("Only Digits")