# 26.checking if all elements in a list are unique


l = [1,2,3,4,5]

if len(l) == len(set(l)):
    print("All elements are unique")
else:
    print("Some elements are repeated")
