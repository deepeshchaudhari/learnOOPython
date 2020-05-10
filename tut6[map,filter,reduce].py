'''
    Map function
    map(function_to_apply,list_of_inputs)
'''
num = [1,2,3,4,0,5,6,2]
sq=[]
for x in num:
    sq.append(x**2)

print('without using map function ',sq)
def square(n):
    return n**2
sq=[]
sq= list(map(square,num))
print('using map function',sq)

