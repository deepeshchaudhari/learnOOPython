a =['a','b','c','d','e']
b= {(1,2),(3,4),(5,66)}
for idx,x in enumerate(a):
    print(idx,x)
for x,y in enumerate(b):
    print(x,y[0],y[1])