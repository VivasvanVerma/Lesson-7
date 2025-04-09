x = 5
if type(x) is int:
    print("True")
else:
    print("False")

p = 3.14
if type(p) is float:
    print("True")
else:
    print("False")

a = 20
b = 20
if a is b:
    print("Same Identity")
b = 30
if a is not b:
    print("Different identity")



