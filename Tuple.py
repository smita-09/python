# Ordered and Immutable
import timeit, sys
tuple1 = (1,2,3)
print(tuple1)
tup2 = tuple([1,2,3])
print(tup2)
# A tuple with just one element is not a tuple anymore, need to add a comma
# Accesing tuple elements are just same as in list
tup3 = ('a','b','c','d','e','a')
print(tup3.count('a'))
print(len(tup3))
print(tup3.index('a'))
# Can also convert list to tuple and tuple to list
tup4 = "smita", 23, "Dresden"
name, age, place = tup4
print(name, age, place)
tup5 = 1,2,3,4,5
i1, *i2, i3 = tup5
print(*i2, i3)
# list consumes more memory than tuple and also more time than tuple
mytupl1 = (1,2,3,4,5)
mylist = [1,2,3,4,5]
print(sys.getsizeof(mytupl1), "bytes")
print(sys.getsizeof(mylist), "bytes")
print(timeit.timeit(stmt= "('1','2','3','4')", number=100000))
print(timeit.timeit(stmt= "['1','2','3','4']", number=100000))