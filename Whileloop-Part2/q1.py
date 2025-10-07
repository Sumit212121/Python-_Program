#wap to count the number of vowels present in the string
# s= 'hello python'

s='hello python'
vowels='aeiou'
i=0
count=0
while i<len(s):
    if s[i] in vowels:
        print(s[i])
        count=count+1
    i+=1
print(count)
