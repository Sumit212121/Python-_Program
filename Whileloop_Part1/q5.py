#wap to print only consonant present inside string s.
#  S='hello guys how are you'

s='hello guys how are you'
i=0
while i<len(s):
    if s[i] not in 'aeiou':
        print(s[i])
    i+=1