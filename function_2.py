def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total*number
    return total


print(multiply(1, 2, 3, 5))
