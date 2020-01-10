sent = False
for i in range(3):
    print("attempt", i)
    if sent:
        print("sent successfully")
        break
else:
    print("i have tried for 3 times ")
