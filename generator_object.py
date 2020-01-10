from sys import getsizeof

values = [x*2 for x in range(10)]
for x in values:
    print(x)
# the list is list [] when thid used but when (useed this is a denerator )

values_2 = (x*2 for x in range(10))
print("the balues of gen", getsizeof(values_2))
print("the size of the list ", getsizeof(values))


# for a big size data base its used

# length object of the generator type is not possible as its a run time
