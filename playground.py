def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 100))


def calculator(p, **kwargs):
    p += kwargs["add"]
    p -= kwargs["sub"]
    p *= kwargs["mul"]
    p /= kwargs["div"]

    #for key, value in kwargs.items():
    #print("Key: " + key + ", Value: " +str(value))
    #print(kwargs["add"])
    #p += kwargs["add"]
    #result *= kwargs["mul"]
    #result /= kwargs["div"]
    return p


print(calculator(4, add=10, sub=2, mul=5, div=2))
