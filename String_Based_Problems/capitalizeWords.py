st = input("Enter a sentence: ")
    
words=st.split()
result=""

for w in words:
    result += w[0].upper() + w[1:] + " "

print(result.strip())