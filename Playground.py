# def add(*args):
#     print((args))
#     sum =0
#     for n in args:
#         sum = n+sum
#     return sum


# print(add(1,2,3,4,5))
# def multiply(n, **kwargs):
    # print((kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# multiply(2,add=5, multiply=6) 


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
