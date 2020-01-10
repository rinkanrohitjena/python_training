# lifo
# fifo

browsing_session = list(range(1, 20, 2))

print("showing the stack", browsing_session)
print("now deleting by lifo . . .")

browsing_session.pop()
print("now showing the stack after delete", browsing_session)
print("now showing the last item in the stack ")
print(browsing_session[-1])
print("now cehcking for the null stack")
if not browsing_session:
    print("not empty so deleting ...")
    for item in browsing_session:
        browsing_session.pop()
        print(browsing_session)

print("stack is empty")
