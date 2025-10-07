# 9. wap tp extract all the special characters present in a string taken as input but
# the user.

s=input("enter the string: ")
specialchar=''
i=0
while i<len(s):
    if 'A' <= s[i] <= 'Z':
        pass
    elif 'a'<= s[i]<='z':
        pass
    elif '0'<=s[i]<'9':
        pass
    else:
        specialchar=specialchar+s[i]

    i+=1

print(specialchar)