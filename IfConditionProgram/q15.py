# 16.wap to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)

num=int(input("enter the number : "))
a=0
if (num % 2 == 0) and (num % 6 ==0):
    print(complex(num))