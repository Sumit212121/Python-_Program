#12.wap to print both upper case and lower case from string

# s = input("Enter a string: ")

# i = 0
# while i < len(s):
#     ch = s[i]
#     if 'A' <= ch <= 'Z':  
#         print(ch, "is Uppercase")
#     elif 'a' <= ch <= 'z': 
#         print(ch, "is Lowercase")
#     i += 1


l=int(input("enter from user"))
i=1
while l >i:
    if l%i == 0:
        print("not prime")
        break
    else:
        print("prime")
    i+=1