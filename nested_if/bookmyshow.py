movies=['war 2','coolie','Narsimha','saiyara']
price=[300,350,250,400]
print("-----------------------WELCOME TO BOOK MY SHOW----------------------")
print(movies[0],' - ',price[0])
print(movies[1],' - ',price[1])
print(movies[2],' - ',price[2])
print(movies[3],' - ',price[3])
ask=input('Select the movie : ')
if ask==movies[0]:
    ticket=int(input("Enter the number of tickets : "))
    if ticket<=60:
        print(f'movie name : {ask}')
        print(f'Price : {price[0]}')
        print(f'Tickets: {ticket}')
        print(f'Total price: {price[0]*ticket}')
        print("thank you for booking the ticket ")
        print("------------enjoy your day------------")
elif ask==movies[1]:
    ticket=int(input("Enter the number of tickets : "))
    if ticket<=60:
        print(f'movie name : {ask}')
        print(f'Price : {price[1]}')
        print(f'Tickets: {ticket}')
        print(f'Total price: {price[1]*ticket}')
        print("thank you for booking the ticket ")
        print("------------enjoy your day------------")
elif ask==movies[2]:
    ticket=int(input("Enter the number of tickets : "))
    if ticket<=60:
        print(f'movie name : {ask}')
        print(f'Price : {price[2]}')
        print(f'Tickets: {ticket}')
        print(f'Total price: {price[2]*ticket}')
        print("thank you for booking the ticket ")
        print("------------enjoy your day------------")
elif ask==movies[3]:
    ticket=int(input("Enter the number of tickets : "))
    if ticket<=60:
        print(f'movie name : {ask}')
        print(f'Price : {price[3]}')
        print(f'Tickets: {ticket}')
        print(f'Total price: {price[3]*ticket}')
        print("thank you for booking the ticket ")
        print("------------enjoy your day------------")