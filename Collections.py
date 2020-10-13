from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))
# easy to created lightweight object typle eg struct
Point = namedtuple('Point', 'x,y') # class with fields x and y
pt = Point(1, -4)
print(pt) # pt.x and pt.y
# less imp but older python version can use it, dict with order
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)
 # similar to dict with default value if key is not set
d = defaultdict(list)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d['u'])
# with normal dict it will raise a key error but i this case it wont
# remove elements form both end
de = deque()
de.append(1)
de.append(2)
print(de)
de.appendleft(3)
print(de)
de.pop()
print(de)
de.popleft()
print(de)
de.clear()
print(de)
de.extend([4,5,6,7,8,9])
print(de)
de.extendleft([1,2,3])
print(de)
de.rotate(1)
print(de)
de.rotate(-1)
print(de)

