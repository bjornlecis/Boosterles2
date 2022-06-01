import random
lijst = []
for i in range(0,100):
    x = random.randint(0,200)
    lijst.append(x)
#print(lijst)
uniek = set(lijst)
print(len(uniek))
lotto1 = {1,14,22,33,44,46,52}
lotto2 = {3,14,23,33,45,48,53}
lotto1.update(lotto1)
print(lotto1)
