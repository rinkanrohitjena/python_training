numbers = [1, 3, 3, 5, 67, 4, 6, 4]
uniques = set(numbers)
second_set = {1, 4}
print(uniques | second_set)
print(uniques & second_set)

print(uniques-second_set)
print(uniques ^ second_set)


if 1 in second_set:
    print("yes")
