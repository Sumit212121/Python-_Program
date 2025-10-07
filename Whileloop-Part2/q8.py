# 7. wap to find the factorial of a number.

num=int(input("enter the number : "))
factorial=1
i=1
while i<=num:
    factorial=factorial*i
    i+=1
print(factorial)