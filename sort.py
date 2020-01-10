# numbers = [3, 51, 64, 63, 26]
# numbers.sort(reverse=True)
# print(sorted(numbers))
# # print(numbers)
items = [
    ("product1", 40),
    ("product2", 57),
    ("product5", 55)
]

filtered = list(filter(lambda item: item[1] >= 50, items))

print(filtered)

# prices = [item[1] for item in items]
# print(prices)
# fid = list(filter(lambda item: item[1] >= 50, items)
# print(fid)
prices_of_good = [item[1] for item in items]

print(prices_of_good)
