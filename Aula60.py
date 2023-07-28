# set (listas)
# similar a listas
# evita itens duplicados
# não utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

print(set1, set2, set3)


print('Union set1 e set2')
set4 = set1.union(set2)
print(set4)

print('Difference entre set1 e set3')
set5 = set1.difference(set3)
print(set5)

print('Intersection set1 com set2')
set6 = set1.intersection(set2)
print(set6)

print('Symetric difference set1 com set3')
set7 = set1.symmetric_difference(set3)
print(set7)

