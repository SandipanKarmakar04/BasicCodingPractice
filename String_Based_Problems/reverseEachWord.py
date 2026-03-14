sent = input("Enter your sentence: ")

words = sent.split()

result = ""

for w in words:
    result += w[::-1] + " "

print(result)


# s = input("Enter a sentence: ")

# word = ""

# for ch in s:
#     if ch != " ":
#         word = ch + word
#     else:
#         print(word, end=" ")
#         word = ""

# print(word)