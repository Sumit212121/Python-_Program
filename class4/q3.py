#wap to check the given number is armstrong number or not.

num=int(input("enter the number : "))
a=num
x=str(num)
z=len(x)
sum=0

while num>0:
    ld=(num%10)**z
    sum=sum+ld
    num=num//10
print(sum)

if a == sum:
    print("it is armstrong number.")
else:
    print("not armstrong")