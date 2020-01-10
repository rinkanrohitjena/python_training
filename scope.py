message = "a"


def greet(name):
    global message
    message = "b"


greet("rohit")
print(message)
