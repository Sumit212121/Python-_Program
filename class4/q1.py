#wap to reverse the number

n=98452
rev=0
while n>0:
    ld=n % 10
    rev= rev*10+ld
    n=n//10
print(rev)