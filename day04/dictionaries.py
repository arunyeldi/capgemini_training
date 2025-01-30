d1 = {}
print(d1)

d2 = {'Virat': 230, 'Rohit': 264}
print(d2)

d3 = {'cricket': {'Hardik': 87, 'Kohli': 98}}
first_pair = list(d3['cricket'].items())[1]
print(first_pair)

k = ['Virat', 'Sachin']
v = ['100', '99']
d = dict(zip(k, v))
print(d)

d4 = dict.fromkeys({'a', 'b'})
d4['a'] = 21
print(d4)

d5 = {'Kohli': 21, 'Hardik': 23}
print(list(d5.keys()))
print(list(d5.values()))

print(d5.get('Kohli'))

d2.update(d5)
print(d2)
print(d1)