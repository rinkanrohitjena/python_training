items_in_cart = [
    ("laptop", 1958), ("iphone", 698), ("doungle", 25)
]
prices_list = []
for item in items_in_cart:
    prices_list.append(item[1])
print("the sorted price list ", sorted(prices_list))


def sort_tuple(item):
    return item[1]


items_in_cart.sort(key=sort_tuple)
print("the sorted tuple as price ", items_in_cart)


total_price = 0
for item in prices_list:
    total_price = item+total_price
print("the total price", total_price)

item_above_500 = list(filter(lambda item: item[1] >= 500, items_in_cart))
print("expansive products", item_above_500)
item_prices_anothermethod = []

items_in_cart.sort(key=lambda item: item[1])
print(items_in_cart)


print("using map function now ....")
only_prices = list(map(lambda item: item[1], items_in_cart))
print(f"using map funtion {only_prices} done")


print("now filter function...")
price_filter = list(filter(lambda item: item[1] >= 500, items_in_cart))
print("the price filterd is now ", price_filter)
print("filter over ")


print("comprehension method... ")
comprehension_method = [item[1] for item in items_in_cart]
print("comprehesnsion method", comprehension_method)
print("list comprehension ends now ...")

print("filtering wtih comprehesnsion...")
filter_comprehensions = [item for item in items_in_cart if item[1] >= 500]
print("filtering with compression op", filter_comprehensions)
print("filtering with filter compression ends now ...")
