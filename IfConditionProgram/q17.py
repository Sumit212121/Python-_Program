# 19.wap to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)

num=int(input("enter the number : "))

if (num%5 == 0) and (num%7==0):
    print(num**2)