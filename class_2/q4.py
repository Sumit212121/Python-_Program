age= int(input("enter the age : "))

if 0 <= age <= 17:
    print("child")
elif 18 <= age <= 30 :
    print("adult")
elif 31 <= age <= 60 :
    print("men")
elif 61 <= age <= 100 :
    print("senior citizen")
else:
    print("invalid ")