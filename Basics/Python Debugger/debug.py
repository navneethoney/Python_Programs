import pdb

x = 3
y = 7
z = [1, 4, 5]

a = x + y
print a

pdb.set_trace()  # To debug the code

b = y + z
print b


# Once it finds pdb.set_trace(), it checks the conditions after it
# Upon doing y + z, it will say "TypeError: unsupported operand type(s) for +: 'int' and 'list' "
