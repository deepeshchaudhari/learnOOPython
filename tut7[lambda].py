'''

syntax :
lambda arguments : manipulation
'''
add = lambda x,y: x+y >y+y
print(add(10,20))

a= [(1,200),(4,5),(55,65)]
a.sort(key=lambda x:x[1]+x[0])
print(a)