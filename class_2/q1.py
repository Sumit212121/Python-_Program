'''str=reverse
   list=append
   tuple=set
   invalid
'''
a =eval(input("enter the data : "))
if type(a) == str:
    print(a[::-1])
elif type(a) == list:
    a.append("ambar")
    print(a)
elif type(a) == tuple:
    print(set(a))
else:
    print("invalid")