import random
""""
kwadraten = []
for i in range(1,21):
    kwadraten.append(i**2)
print(kwadraten)
"""
"""
lijst=[]
som = 0
for i in range(0,20):
    rnd = random.randint(1,100)
    lijst.append(rnd)
    som += rnd
print(lijst,som,som/20)
"""
even = []
oneven = []
max_even = 0
max_oneven = 0

for k in range(0,1000):
    for i in range(0,100):
        rnd = random.randint(0,100)
        if rnd%2==0:
            even.append(rnd)
        else:
            oneven.append(rnd)

    if max_even < len(even):
        max_even = len(even)
    if max_oneven < len(oneven):
        max_oneven = len(oneven)
    even.clear()
    oneven.clear()

#print("lijst even bevat {} items\nlijst oneven bevat {} items".format(len(even),len(oneven)))
print("het max aantal even getallen was {}\nhet max aantal oneven getallen was {}".format(max_even,max_oneven))

