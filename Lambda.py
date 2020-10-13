# lambda arguments: expressions
add10 = lambda x: x+10 # much shorter and only in one line
print(add10(5))

mul = lambda x,y: x*y
print(mul(2,3))
points2D = [(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted = sorted(points2D,key=lambda x:x[1]) # to get it printed on the basis of second index
print(points2D)
print(points2D_sorted)

# can also be used with a map
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))
c = [x*2 for x in a]
print(c)
d = filter(lambda x: x%2 == 0, a)
print(list(d))