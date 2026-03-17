st = input()
sbst = input()

if sbst in st:
    print("found", st.find(sbst))
else:
    print("Not found")