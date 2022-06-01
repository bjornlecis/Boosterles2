#y = lambda x: x+2

#for i in range(0,11):
#    print(y(i))

oppv = lambda b,h:(b*h)/2
print(oppv(5,4))

f1 = lambda x,y:x*2+y
f2 = lambda x,y:x**2+y**2
f3 = lambda x,y:x**2+2*x*y+y**2
f4 = lambda x: x/3 if x%3==0 else x*2
f5 = lambda x,y: x/2 if x>y*2 else x*2
print(f5(8,5))
