a = ['Zob', 'Bob', 'Martine']
a1 = a
b = ['Paul', 'Jack']
nums = [1, 5, 18, 9, 6, 7]
# Add an item
a.append('Dylan')

# Inserting to a specified index
a.insert(0,'Vase')

# Extending a list to a list
a.extend(b)

# Remove values
a.remove('Martine')

# Return the removed element of the list
pop = a.pop()
print(pop)

# Reverse a list
a.reverse()
print(a)

# Sort number
nums.sort(reverse=True)
print(nums)

# Get a sorted version of the list without altering the list
sortedList = sorted(a)
print(sortedList)

# Get an index
indexBob = sortedList.index('Bob')
print("Index of Bob is " + str(indexBob))

# Check if something is in the list
print('Dylan' in sortedList)

# Iterate through list
for index, name in enumerate(sortedList, start=1):
    print(index,name)

# From list to string
name_str=' - '.join(sortedList)
print(name_str)

# From string to list
new_list = name_str.split(' - ')
print(new_list)

# List are mutable
# Tuple are immutable

a[0]='Mickey'
# a1 is a reference to the same mutable object so if a changes a1 too
print(a1)
# If we want a list with fixed values we can use tuple
tuple1 = ('Math', 'Physic', 'IT Science')
tuple2 = tuple1

print(tuple1)
# Sets remove duplicate and don't have orders
# Sets are optimals to check if a value is in the set
set1 = {'Math', 'Physic', 'IT Science'}
set2 = {'Design', 'Physic', 'IT Science'}
# set can do intersection

innerjoin = set1.intersection(set2)
difference = set1.difference(set2)
union = set1.union(set2)
print(innerjoin,difference,union)

# Empty Stuff

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()