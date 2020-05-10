from functools import reduce
def mul(a,b):
    return a*b

consecutive_data_sum = reduce(mul,[1,2,3,4,5,6,7,8,9])
print(consecutive_data_sum)