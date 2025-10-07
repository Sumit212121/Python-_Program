# 11.wap to print a number which are divisible by 5 from a list
# l=[63,20,67,55,85,31]

l=[63,20,67,55,85,31]

i=0
while i<len(l):
    if l[i] % 5 == 0:
        print(l[i])
    i+=1