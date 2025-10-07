# wap to print the elements which in tuple,print only the if it is collection data
# types

# values=(10,2.5,[10,20],"hero",True,(3,4,5),{2,7},{90:"super"})


values=(10,2.5,[10,20],"hero",True,(3,4,5),{2,7},{90:"super"})
i=0
while i<len(values):
    if type(values[i]) in [str,tuple,set,list,dict]:
        print(values[i])
    i+=1