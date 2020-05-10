'''
    Iterable-
            __getitem
    Iterator-
            next
    Iteration-
'''
#make object and generate value on the go....with out using more ram
def gen(n):
    for i in range(n):
        yield i
obj =gen(100)
print(next(obj))
print(next(obj))
num = "deepesh"
iter1 = iter(num)
print(next(iter1))
print(next(iter1))
print(next(iter1))
