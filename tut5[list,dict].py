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