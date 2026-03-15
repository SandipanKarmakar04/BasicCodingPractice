no = int(input("Enter a number to check for strong: "))

temp = no
summ = 0

while temp > 0:
    digit = temp % 10 #this seperates all the digits
    fact=1
    i=1
    
    while i <= digit: #this section multiply all the digits till the individual digits it stored
        fact *= i
        i += 1
        
    summ += fact
    temp = temp // 10

if summ == no:
    print("Strong Number")
else:
    print("Not a strong number")