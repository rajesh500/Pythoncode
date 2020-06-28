if __name__=='__main__':
    n = input("Enter your input numbers to find the smallest number:")  # user data read always as string
    m = n.split()   # taking multiple values in list, split default splits data into list
    a = int(m[0])   # taking first value
    for i in range(len(m)):  # looping
        b = int(m[i])    # taking again first value
        if b < a:    # always first iteration,  will fail
            a = b     # for second iteration swapping values, a value holds least value and b will get new values from the list.
    print("The smallest number is:", a)   # b > a print largest value




