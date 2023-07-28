# set (listas)
# similar a listas
# evita itens duplicados
# não utiliza index
# convertendo para set "list1 = set([1, 2, 3, 5, 6])"
# em set numeros duplicados não aparecem
# discard() não apresenta erro nos que não existem

list1 = [1, 2, 3, 5, 6]
s1 = {1, 2, 3, 4, 5, 6}
s1.add(7)
s1.update([8, 9, 10])

print(list1)
print(s1)
print(type(list1))
print(type(s1))

s1.remove(8)
print(s1)
s1.discard(10)
print(s1)
