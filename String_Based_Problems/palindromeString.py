st=input("Enter a string to check for palindrome: ")

# if st == st[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

rev = ""

for ch in st:
    rev = ch + rev

if st == rev:
    print("palindrome")
else:
    print("not palindrome")