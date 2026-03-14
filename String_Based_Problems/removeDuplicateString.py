string = input()

uniq = ""

for c in string:
    if c not in uniq:
        uniq += c
print(uniq)
