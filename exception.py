# try:
#     age = int(input("enter the age :"))
# except ValueError:
#     print("you did not entered a valid entry ")
# else:
#     print('THE AGE IS ',    age)
# print("program continuees now ")

# try:
#     state = input("enter your state ")
# except ValueError as ex:
#     print("you have entered invalid inter ")
#     print(ex)
#     print(type(ex))
# else:
#     print("the statement ", state)

try:
    file = open("exception.py")
    age = int(input("enter the age :"))
    result = 10/age
    print("the result", result)
    file.close()
except (ValueError, ZeroDivisionError):
    print("you did not entered a valid entry ")
else:
    print('THE AGE IS ',    age)
finally:
    file.close()
# this is the place to close file connections , network connections , data base connections and all .
