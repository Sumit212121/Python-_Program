#wap to find the factorial of a number taken as input .

num=int(input("enter the number : "))

factorial=1
i=1
while i <num+1:
    factorial=factorial*i
    i+=1
print(factorial)