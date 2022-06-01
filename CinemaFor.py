aantal_per = int(input("geef het aantal personen in"))
totaalprijs = 0
for i in range(0,aantal_per):
    leeftijd = int(input('geef de leeftijd in'))
    prijs = 0

    if leeftijd < 13:
        prijs = 4
    elif leeftijd < 19:
        prijs = 5
    else:
        prijs = 6

    lsf = input("is het een lang speelfilm j/n")
    if lsf == "j":
        prijs += 2
    ddf = input("is het een 3d film j/n")
    if ddf == "j":
        prijs += 2
    stud_kaart = input("heb je een studentenkaart j/n")
    if stud_kaart == "j":
        prijs -= 2
    print(prijs)
    totaalprijs += prijs

print(totaalprijs)
