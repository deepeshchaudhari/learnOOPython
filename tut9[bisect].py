'''

Bisect module
'''
import bisect
a= [1,2,3,44,5,7,8,9]
number = 6
print(bisect.bisect(a,number))
bisect.insort(a,number)
print(a)