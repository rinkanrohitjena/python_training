product_list = ["laptop", "nintendo", "iphone", "ipad"]
price_list = [4500, 3400, 530, 199]


# usin zip
print("using zip funcion")
item_list = list(zip(product_list, price_list))
print("using the zip funstiont to bind the two lists{item_list}...", item_list)


# we can pass a string as a string is ittrable too
print("passing a string into the zip function..")
item_new = list(zip("amazon", price_list))
print(
    "using the zip function to iratate over a string {item_list}...", item_new)


# zip over
