# 5.wap to extract only vowels and digits from the given string
# s="hellopython123"

s="hellopython123"
i=0
while i<len(s):
    if s[i] in 'aeiou':
        print(s[i])
    elif s[i] in '1234567890':
        print(s[i])
    i+=1