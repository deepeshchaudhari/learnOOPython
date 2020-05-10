'''
    List comprehension
    Dictionary comprehension
    Set comprehension
    Generator comprehension
'''
list =[1,2,3,2,1,32,3,1,25,45,1,32,54,1,2,54,1,5,21,5]
div_by_3=[]
for x in list:
    if x%3==0:
        div_by_3.append(x)
print(div_by_3)
print('without using list comprehension',div_by_3)
print('using list comprehension',[x for x in list if x%3==0])

dict1 = {'a':45,'b':65,'A':15}
print(dict1['a'])
print({k.lower(): dict1.get(k.lower(),0) + dict1.get(k.upper(),0) for k in dict1.keys()})

squared = {x**2 for x in [1,2,1,2,3,5,4,7,7]}
print(squared)
# create only object and save memory but take more time
gen = {i for i in range(56) if i%3==0}

for item in gen:
    print(item)