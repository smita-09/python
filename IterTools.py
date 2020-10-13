from itertools import product, permutations, combinations, combinations_with_replacement
from itertools import accumulate, groupby, count, cycle, repeat
import operator
a = [1,2]
b = [3]
prod = product(a,b, repeat=2)
print(list(prod))
# all possible orderings  of input
a = [1,2,3]
perm = permutations(a, 2)
print(list(perm))
b = [1,2,3,4]
comb = combinations(b,2)
print(list(comb)) # its just repetitions is not allowed
comb_wr = combinations_with_replacement(b,2)
print(list(comb_wr))
acc = accumulate(b, func=operator.mul) # multipy as well
print(b)
print(list(acc))
# makes an iterator that return keys
def smaller_than_3(x):
    return x < 3

c = [1,2,3,4]
grp_obj = groupby(c, key=smaller_than_3) # key = lambda x: x < 3
print(grp_obj)
for key, value in grp_obj:
    print(key, list(value))
#  Also look at these funcs, thesea re easy(cycle, repeat, count)

