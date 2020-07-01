# *args(non - keyworded arguments) & ** kwargs(keyworded arguments)

def fun(*args):
    for i in args:
        print("Hi, Arguments are:", i)


fun("Rajesh", "J")


def fun(**kwargs):
    for i, j in kwargs.items():  # must and should i , j in loop
        # print(j) # values
        # print(i) # keys
        print(i, j)
        print("Name is", j)
        print(type(j))


fun(First="Rajesh", Last="J")  # finally, data is in the tuple