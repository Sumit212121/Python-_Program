#wap to check a data is a sequence(mutable),/iterable(immutable),individual datatype 

a = eval(input("enter the data : "))

if type(a) == list:
    print("it is sequence")
elif type(a) == set :
    print("mutable datatype")
elif type(a) == dict :
    print("mutable")
elif type(a) == str:
    print("immutable type")
elif type(a) == tuple:
    print("immutable type")
else:
    print("individual type")