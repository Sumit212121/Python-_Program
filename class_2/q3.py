a =eval(input("enter the data: "))

if type(a) == str:
    print(len(a))
elif type(a) == list:
    a.pop()
    print(a)
elif type(a) == tuple:
    print(a[::-1])
else:
    print("invalid input")