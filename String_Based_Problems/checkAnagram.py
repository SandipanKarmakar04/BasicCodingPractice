s1 = input()
s2 = input()

count = 0

if len(s1) != len(s2):
    print("Its not anagram")
else:
    for i in s1:
        if i in s2:
            count += 1    
    if count == len(s1):
        print("Anagram")
    else:
        print("Not an anagram")