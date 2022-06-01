def toon_menu():
    print("1: toon de lijst")
    print("2: voeg naam toe")
    print("3: is persoon in lijst")
    print("4: verwijder persoon uit de lijst")
    print("5: vervangen naam door")
    print("6: sorteer de lijst a-z")
    print("7: zoek op beginletter")

def toon_lijst(l):
    for x in l:
        print(x)
def voeg_naam_toe(l:list):
    naam = input("geef de naam")
    l.append(naam)
def is_persoon_in_lijst(l:list):
    persoon = input("geef de naam van de persoon")
    if persoon in l:
        print("persoon is in de de lijst")
    else:
        print("persoon is niet in de de lijst")
def verwijder_persoon_uit_lijst(l:list):
    persoon = input("geef de naam van de persoon")
    for x in l:
        if x==persoon:
            l.remove(x)

def vervang_naam_door(l:list):
    naam = input("geef de naam waarin je wilt vervangen")
    nieuwe_naam = input("geef de nieuwe naam in")
    for x in l:
        if x == naam:
            index = l.index(naam)
            l[index] = nieuwe_naam
def zoek_op_beginletter(l:list):
    begin_letter = input("geef een begin letter in")
    filter = []
    for x in l:
        if begin_letter == x[0]:
            filter.append(x)
    return filter

lijst = ["Ben","An","Jan","Sofie","Ben","Jos","Joske","Mark","Bart","Frank"]
lijst2 = ["Jef","Mark","Sonja"]

opdracht = ""
toon_menu()
while(not opdracht=="stop"):
    opdracht = input("geef de opdracht in")
    if opdracht == "stop":
        break
    elif opdracht == "1":
        lijst_num = input("lijst 1 of 2")
        if lijst_num == "1":
            toon_lijst(lijst)
        else:
            toon_lijst(lijst2)
    elif opdracht == "2":
        voeg_naam_toe(lijst)
    elif opdracht == "3":
        is_persoon_in_lijst(lijst)
    elif opdracht == "4":
        verwijder_persoon_uit_lijst(lijst)
    elif opdracht == "5":
        vervang_naam_door(lijst)
    elif opdracht == "6":
        lijst.sort()
    elif opdracht == "7":
        print(zoek_op_beginletter(lijst))
    else:
        print("opdracht niet gekend")
