# unordered and mutable and no duplicates
set1 = {1,2,3,4,5}
print(set1)
set2 = {1,1,1,1}
print(set2)
set3 = set("hello")
print(set3)
# empty set is recognised as dict
# discard and remove methods
print(set3.pop())
odds = {1,3,5,7,9}
evens = {2,4,6,8,10}
primes = {2,3,5,7,11}
u = odds.union(evens)
i = odds.intersection(evens)
print(i,u)
diff = primes.difference(evens)
print(diff)
symdiff = primes.symmetric_difference(evens)
print(symdiff)
# frozensets are immutable