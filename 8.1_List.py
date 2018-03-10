List - Collection

friends = ['a', 'b', 'c']

for i in range(len(friends)) :
    friend = friends[i]
    print(friend)

# >>> range(len(friends))
# [0, 1, 2]

Concatenation -- Slicing
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']
