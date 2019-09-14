
user = 'Root'
logged_in = True

if user == 'Root' and logged_in:
    print(user + ' is logged in ...')
else:
    print('Wrong credentials')
    exit(1)

a = [1, 2, 3]
b = [1, 2, 3]

print( a is b)
# not the same in memory

print(id(a))
print(id(b))

# False Values
# False None Zero '' () [] {}