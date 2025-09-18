# 28. WAP to check whether a character is in uppercase or not

ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z':   
    lower = ch.lower()       
    d = {lower: ord(lower)}  
    print("Dictionary:", d)
else:
    print("Not an uppercase character")
