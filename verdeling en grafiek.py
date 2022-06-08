import numpy as np
import matplotlib.pyplot as plt
lijst = np.random.randint(100, size=10)
lijsta = []
lijstb = []
lijstc = []
lijstd = []
lijsten = [lijsta,lijstb,lijstc,lijstd]

for x in lijst:
    if x < 25:
        lijsta.append(x)
    elif x < 50:
        lijstb.append(x)
    elif x < 75:
        lijstc.append(x)
    else:
        lijstd.append(x)

lijst_aantallen = []
for x in lijsten:
    print(x)
    lijst_aantallen.append(len(x))

print(lijst_aantallen)



fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
label = ['<25', '25-49', '50-74', '74-99']
ax.bar(label,lijst_aantallen)
plt.show()
