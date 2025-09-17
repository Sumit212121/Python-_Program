# 10.wap to check if the given string is palindrome (take user input)

st=input("enter the string : ")
if st == st[::-1]:
    print("palindrom")
else:
    print("not palindrome")