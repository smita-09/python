#lists are ordered, mutable
mylist = [1,2,4,5]
print(mylist)
mylist1 = list()
mylist1 = [1, "smita", 5.6]
# Indices will be usual, there is just one more index with which you can acess last element
print(mylist1[-1])
for items in mylist1:
    print(items)
if "smita" in mylist1:
    print("yes")
# Methods to add elements to list are insert and append and len to acces the length of the list
# Methods to remove elements from the list are .pop() and .remove() with idx mentioned with it
# clear method is to clear the whole list i.e mylist1.clear()
# .reverse() is a method to reverse the list and sort to sort the list and can also be done in place
# in case you wan it to change not in place
print(sorted(mylist))
# Normal slicing methods are also used to acces the list
# list1 = list2, copying this way will lead to two list sharing same memory
# list1.copy(), will not lead o above case.
lis1 = [1,2,3,4,5,6]
list2 = [i*i for i in lis1]
print(list2)


