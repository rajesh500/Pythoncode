a=1000
def add(a, b):
    print("SUM is ", a+b)

def sub(a, b):
    print("Difference", a-b)

def mul(a, b):
    print("Multiply", a*b)

def div(a, b):
    print("Divide", a/b)

print("All this methods/members from to module.py")
print(dir())
if __name__=='__main__':
    add(10, 20)
    sub(20,10)
    mul(10, 20)
    div(20,10)