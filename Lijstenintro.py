""" lijst gebruiker input
lengte = int(input("geef het aantal getallen in"))
lijst = []

def toon_lijst():
    for x in lijst:
        print(x)

toon_lijst()
for i in range(0,lengte):
    getal = int(input("geef getal"))
    lijst.append(getal)

toon_lijst()
lijst.append(9)
toon_lijst()
"""
cars = ["Ford", "Volvo", "BMW","Fiat","Ford","Ford","Volvo"]
tel = 0
for x in cars:
    print(type(x))


print(tel)
