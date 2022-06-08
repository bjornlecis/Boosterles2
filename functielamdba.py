import matplotlib.pyplot as plt

y = lambda x:(x**3)-5
lijn_y = []

for i in range(0,20):
    lijn_y.append(y(i))

plt.plot(lijn_y, linestyle = 'dotted')
plt.show()
