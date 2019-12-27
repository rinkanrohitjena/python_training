#number_range = int(input(">"))
#count = 0
# for i in range(2, number_range, 2):
#   print("the number is ", i)
#  count = count + 1
#print("the total ever number are ", count)
limit = int(input(">>"))
count = 0
for number in range(1, limit):
    if number % 2 == 0:
        print(number)
        count = count+1
print(f"Thee are {count}numbers of even number")
