# Immutable and ordered
my_string = """Hello \
world"""
print(my_string)
# Accesing happens in the usual way
# .strip removes whitespaces and doesnt happen inplace
# .upper, .lower, .isupper, .startswith,
my_string1 = "hello world"
print(my_string1.find('lo')) # if not then returns -1
print(my_string1.count('o'))
print(my_string1.replace('o', 's'))
print(my_string1.split())
print(' '.join(my_string1))
var1 = 2
var2 = 3.686
print("these are two vars {} {}".format(var1, var2))
print(f"these are two vars {var1} and {var2}")
