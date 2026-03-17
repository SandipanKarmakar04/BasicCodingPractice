# Example:
# Input: sandipan
# output: sandip    a and n will not come second time.
string = input()

uniq = ""

for c in string:
    if c not in uniq:
        uniq += c
print(uniq)
