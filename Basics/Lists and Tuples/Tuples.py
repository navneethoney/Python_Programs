# Tuples are same as Lists and Tuples but only difference is tuples are immutable

tup1 = (1, 2, 3, 7.8, 'five')
print(tup1)

print(tup1[2])
print(tup1[-1])

print(len(tup1))

tup2 = ('a', 'a', 'b')
print(tup2.count('a'))
print(tup2.index('a'))

tup3 = ('a', 2, [1.4, 'three', 9])
print(tup3)
print(tup3[2])
print(tup3[2][1])