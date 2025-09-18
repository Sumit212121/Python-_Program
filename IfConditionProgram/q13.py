
# 13.wap to check the given value is string (take user input)

# 13. WAP to check the given value is string (take user input)

value = input("Enter something: ")

# input() hamesha string deta hai
if isinstance(value, str):
    print("Yes, the given value is a string.")
else:
    print("The given value is not a string.")

