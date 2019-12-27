def greet(first_name):

    print(f"hi {first_name} there")
# perfoming a task
# calculate and return a vlaue


def greeting(name):
    return f"hi{name}"


message = greeting("volu")
file = open("/root/Desktop/python/exer.txt", "w")
file.write(message)
