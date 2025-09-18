

# 17. WAP to check whether the given number is even or not,
# if even store the value inside the list (take user input)

num = int(input("Enter the number: "))
l = []

if num % 2 == 0:
    l.append(num)   # directly append
    print("Updated list:", l)
else:
    print("The number is odd, so not stored in list.")
