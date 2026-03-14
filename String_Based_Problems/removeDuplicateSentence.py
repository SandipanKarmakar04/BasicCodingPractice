string = input()

words = string.split()

uniq = ""

for w in words:
    if w not in uniq:
        uniq += w + " "
print(uniq)