# 27. WAP to check whether a character is in the alphabet or not,
# if it is alphabet, store the value inside a dict 
# (key as character and value as ASCII value)

ch = input("Enter a character: ")
d={}
if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):  
    d[ch]=ord(ch) 
    print("Dictionary:", d)
else:
    print("The given character is not an alphabet.")
