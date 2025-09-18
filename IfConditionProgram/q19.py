# 20.wap to check whether a given value is present in between 45 and 200 and the number should be divisible by 4 and 5 ,if satisfied,display the ascii chracters (take user input)

num=int(input("enter the number : "))

if 45 <= num <= 200:
    if (num%4 ==0) and (num%5==0):
        print(num ,'ascii value is ',chr(num))