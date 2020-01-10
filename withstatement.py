try:
    with open("exception.py") as file:  # independent of finallay clause
        print("file opened.")
    age = int(input("enter the age :"))
    result = 10/age
    print("the result", result)
    file.close()
except (ValueError, ZeroDivisionError):
    print("you did not entered a valid entry ")
else:
    print('THE AGE IS ',    age)
