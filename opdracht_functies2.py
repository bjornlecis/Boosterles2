import math
def balk_inhoud(b,h,d,p=None):
    if p is not None:
        return b*h*d*p/100
    else:
        return b*h*d
def teken(x:int,tekst:str):
    if x > len(tekst):
        print("De tekst is kleiner dan de gevraagde plaats")
    else:
        print(tekst[x-1])

#print("de oppervlakte is {} m³".format(balk_inhoud(10,5,2,35)))
#teken(2,"Hallo")

def schuine_zijde(x:float,y:float):
    print("de schuine zijde is",round(math.sqrt(x**2+y**2),2))

schuine_zijde(12,16)
