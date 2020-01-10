numbers = [x for x in range(1, 30)]
print(numbers)
print(*numbers)
# unpacking the list now
new_list = [*range(5), *"hello"]
print(new_list)

combine = [*numbers, *new_list]
print(combine)


# use to take out the individual values of any ittarable
