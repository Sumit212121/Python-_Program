#wap  to check if a number is taken as input is palindrom or not.

num=int(input("enter the number : "))
a=num
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)
if a == rev:
    print("palindrome")
else:
    print("not")
