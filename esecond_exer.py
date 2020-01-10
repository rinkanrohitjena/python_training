
sentence = input("enter your string >>")
letter = input("enter your letteer>>")
count = 0
countlist = [x for x in sentence]
for x in countlist:
    if x == letter:
        count = count+1

print("the number of time appeared ", count)
