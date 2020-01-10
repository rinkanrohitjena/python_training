from timeit import timeit

code1 = """

def calculate_factor(age):
    if age <= 0:
        raise ZeroDivisionError("value caant be zero")
    return 10/age


try:
    calculate_factor(-1)
except (ValueError, ZeroDivisionError) as Error:
    # print(Error)
    pass
"""
print(timeit(code1, number=10000))

code2 = """

def calculate_factor(age):
    if age <= 0:
        return None
    return 10/age


xfactor = calculate_factor(-1)
if xfactor==None:
    pass
"""
print(timeit(code2, number=10000))
