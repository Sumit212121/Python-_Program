joining=int(input("year of joining "))

exp=2025- joining
print("experience is",exp)

if 0 <= exp <= 2:
    print(" no hike in salary")
elif 3 <= exp <= 5:
    print("hike of 5000")
elif 6 <= exp <= 8:
    print("hike of 7000")
elif 9 <= exp :
    print("hike of 10000")
