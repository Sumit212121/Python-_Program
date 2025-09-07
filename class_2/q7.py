m1 =int(input(" enter the first marks : "))
m2 =int(input(" enter the second marks : "))
m3 =int(input(" enter the third marks : "))
m4 =int(input(" enter the fourth marks : "))
m5 =int(input(" enter the fifth marks : "))

total = 500
avg=((m1+m2+m3+m4+m5)/5)

if 90 <= avg <= 100:
    print("distinction")
elif 75 <= avg <= 89:
    print("firstclass")
elif 60 <= avg <= 74:
    print("second division")
elif 50 <= avg <= 59:
    print("third division")
elif avg<50:
    print("fail")