s = input("Enter string: ")

max_len = 0

for i in range(len(s)):
    sub = ""
    for j in range(i, len(s)):
        if s[j] not in sub:
            sub += s[j]
            max_len = max(max_len, len(sub))
        else:
            break

print("Longest substring length:", max_len)