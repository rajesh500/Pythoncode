# *args(non - keyworded arguments) & ** kwargs(keyworded arguments)
from sys import argv
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

def argv_ex(argv):
    print(" This is argv argument:", argv)

if __name__=='__main__':
    argv_ex(10)

# argv can be used from terminal as well, if we running python code by using terminal with file_name.py
# we can pass argument with file name example unix positional arguments.
