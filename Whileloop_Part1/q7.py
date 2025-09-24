#wap to print only multivalued data items present inside 
#  a list taken as input from user.

lst=eval(input("enter the list : "))
i=0
while i<len(lst):
    if type(lst[i]) in [str,set,tuple,list,dict]:
        print(lst[i])
    i+=1             

