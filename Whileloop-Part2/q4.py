# 3.wap to print the name which is starting with vowel in the given list
# names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]

names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]

i=0
while i<len(names):
    if names[i][0] in 'aeiou':
        print(names[i])
    i+=1