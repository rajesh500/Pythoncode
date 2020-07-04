# String Data Type:
s=input("Please enter something here:")
print(s.strip())
print(s.rstrip())
print(s.lstrip())
print(s.find("is"))  # index("is")
print(s[0])
print(s.count('a'))  # atleast one argument
print(s.replace("bad", "good"))
print(s.split('-'))
a=s.split('-')
#  for i in range(3):print(i)
for i in a:
    print(i)
b='/'.join(s)   # need to take value in list
print(b)
print(s.replace('-', '/'))
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print(s.startswith("python"))
print(s.endswith("easy"))
if s.isalnum():
    print("True")
else:
    print("False")
if s.isalpha():
    print("True")
else:
    print("False")
if s.isdigit():
    print("True")
else:
    print("False")
if s.islower():
    print("True")
else:
    print("False")
if s.isupper():
    print("True")
else:
    print("False")
if s.istitle():
    print("True")
else:
    print("False")
if s.isspace():
    print("True")
else:
    print("False")

a="Rajesh"
b="J"
print("{} {}".format(a,b)) # format can be used in different way( calling method, class)

#