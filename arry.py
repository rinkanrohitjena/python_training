from array import array


numbers = array("i", [1, 2, 3, 4])


# takes less memory and perfomes faster above 10000 numbers
numbers.remove(2)
print(numbers)
