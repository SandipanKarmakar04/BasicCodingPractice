st = input("Enter the string to count vowel consonent: ").lower()

vowel = 0
consonent = 0

for i in st:
    if i in "aeiou":
        vowel += 1
    elif i.isalpha():   #this check whether the character is an alphabate or not.
        consonent += 1

print("Vowels: ",vowel)
print("Consonents: ",consonent)