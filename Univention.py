import random
x = random.randint(0,100)
n = 0
tries = 0
while (n == 0):
    tries = tries+1
    inputnumber =int(input("Gib eine Zahl an: "))
    if inputnumber > x:
        if inputnumber < 101:
            print("Die gesuchte Zahl ist kleiner.")
        if inputnumber > 100:
            print("Die gesuchte Zahl ist nicht größer als 100")
    if inputnumber < x:
        if inputnumber > -1:
            print("Die gesuchte Zahl ist größer")
        if inputnumber < 0:
            print("Die gesuchte Zahl ist größer als 0")
    if inputnumber == x:
        print("Wir haben einen Gewinner!")
        print("Anzahl der Versuche: " + str(tries))
        break
