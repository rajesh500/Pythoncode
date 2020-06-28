# def number(self, num):
#     return num

import datetime
date=datetime.datetime.now()

if __name__=='__main__':
    name="Rajesh "
    last='J'
    con='USA'
    print("My name is {} {}, I am from {}".format(name, last, con))
    print("Directly, number passed to the operator from the format method {}".format(100))
    print("Giving space: {:d}".format(1000))
    print("Giving 5 tabs spacce: {:5d}".format(1000))   # given four digit, but fifth digit is space add in MSB
    print("Floating first 8 digits and floating values are 4:{:08.4f}".format(123.24516282))
    dictnry={"num":100, 'name':'Rajesh J'}
    print("My name is {d[name]} and number is {d[num]}".format(d=dictnry))  # dictionary can be called in two ways
    print("Second way, My name is {name} and My number is {num}".format(**dictnry))
    # print("My name is {d.name} and number is {d.num}".format(d=dictnry))  #dictionary keys we can't call like this
    print("Time is {:%d/%m/%Y %H:%M:%S}".format(date))
    print("Time is {}".format(date))
    print("Today's date is:", date)
    print(date.strftime('%d/%m/%Y'))