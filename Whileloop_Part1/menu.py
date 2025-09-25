Menu = ['Maggie','Pizza','Burger','Litti chokha']

price= [50,99,59,30]
print('-----------------WELCOME TO FOOD CORNER---------------')
print(Menu[0],' - ',price[0])
print(Menu[1],' - ',price[1])
print(Menu[2],' - ',price[2])
print(Menu[3],' - ',price[3])

Name=input("Enter you name : ")
Phone_no=int(input("your phone number : "))
Address=input("Enter your address : ")

ask=input('Select the food items :')
if ask ==Menu[0]:
    quantity=int(input("Enter the number of food items: "))
    if quantity<=20:
        print(f'Items name : {ask}')
        print(f'price: {price[0]}')
        print(f'quantity : {quantity}')
        print(f'Total price : {price[0]*quantity}')
        print("-----------------------THANK YOU FOR VISITING---------------")
elif ask ==Menu[1]:
    quantity=int(input("Enter the number of food items: "))
    if quantity<=20:
        print(f'Items name : {ask}')
        print(f'price: {price[1]}')
        print(f'quantity : {quantity}')
        print(f'Total price : {price[1]*quantity}')
        print("-----------------------THANK YOU FOR VISITING---------------")
elif ask ==Menu[2]:
    quantity=int(input("Enter the number of food items: "))
    if quantity<=20:
        print(f'Items name : {ask}')
        print(f'price: {price[2]}')
        print(f'quantity : {quantity}')
        print(f'Total price : {price[2]*quantity}')
        print("-----------------------THANK YOU FOR VISITING---------------")
elif ask ==Menu[3]:
    quantity=int(input("Enter the number of food items: "))
    if quantity<=20:
        print(f'Items name : {ask}')
        print(f'price: {price[3]}')
        print(f'quantity : {quantity}')
        print(f'Total price : {price[3]*quantity}')
        print("-----------------------THANK YOU FOR VISITING---------------")
