# 3.wap to check if the student has scored 70% print "good luck "(take user input)

m1=int(input("enter the first marks: "))
m2=int(input("enter the second marks: "))

total=((m1+m2)/200)*100

if total == 70:
    print("good luck")
else:
    print("nothing")