'''
    filter function
'''
def greater_than_2(n):
    if n>2:
        return True
    else:
        return False
l = [1,2,12,1,2,1,2,1,222,1,2,1,2]
gt = list(filter(greater_than_2,l))
print(gt)

