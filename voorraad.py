producten = {"appel":50,"peer":20,"banaan":35}
def toon_producten():
    for x in producten.items():
        print(x)
def voeg_product_toe():
    naam = input("geef de naam van het product")
    aantal = int(input("geef het aantal van het product"))
    producten[naam] = aantal
def wijzig_aantal():
    naam = input("geef de naam van het product")
    if naam in producten.keys():
        aantal = int(input("geef het nieuwe aantal van het product"))
        producten[naam] = aantal
    else:
        print("foutieve productnaam")
def voeg_aantal_toe():
    naam = input("geef de naam van het product")
    if naam in producten.keys():
        aantal = int(input("geef het nieuwe aantal van het product"))
        producten[naam] += aantal
    else:
        print("foutieve productnaam")
def verwijder_product():
    naam = input("geef de naam van het product")
    if naam in producten.keys():
        producten.pop(naam)
    else:
        print("foutieve productnaam")

opdracht = ""
while(not opdracht=="stop"):
    opdracht = input("geef de opdracht in")
    if opdracht == "stop":
        break
    elif opdracht == "1":
        toon_producten()
    elif opdracht == "2":
        voeg_product_toe()
    elif opdracht == "3":
        wijzig_aantal()
    elif opdracht == "4":
        voeg_aantal_toe()
    elif opdracht == "5":
        verwijder_product()
    else:
        print("opdracht niet gekend")
