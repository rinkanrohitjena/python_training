items = [("product1", 45), ("product4", 65), ("product5", 75)]

prices = []
for item in items:
    prices.append(item[1])


map(lambda item: item[1], items)
print(prices)
