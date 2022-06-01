def toon_menu():
    print("1: tonen van de tupple")

def toon_tuple(t:tuple):
    for x in t:
        print(x)
def voeg_merk_toe(t:tuple):
    merk = input("geef het merk")
    l = list(t)
    l.append(merk)
    return tuple(l)

def zoek_in_tuple(t:tuple):
    merk = input("geef het merk dat je wenst te zoeken")
    if merk in t:
        print("merk in tupple")
    else:
        print("merk niet in tupple")
def verwijder_in_tupple(t:tuple):
    merk = input("geef het merk dat je wenst te verwijderen")
    l = list(t)
    for x in l:
        if merk == x:
            l.remove(x)
    return tuple(l)


automerken = ("bmw","ford","mazda","fiat","audi")

opdracht = ""
while not opdracht == "stop" or opdracht == "STOP":
    opdracht = input("geef opdracht in")
    if opdracht == "stop" or opdracht == "STOP":
        break
    elif opdracht == "1":
        toon_tuple(automerken)
    elif opdracht == "2":
        automerken = voeg_merk_toe(automerken)
    elif opdracht == "3":
        automerken = zoek_in_tuple(automerken)
    elif opdracht == "4":
        automerken = verwijder_in_tupple(automerken)
    elif opdracht == "5":
        l = list(automerken)
        l.sort()
        l.reverse()

        automerken = tuple(l)



