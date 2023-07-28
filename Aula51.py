# Umpacking lists - desempacotar listas
# Armazenar mais de uma informação em variáveis
# Manter a sequência dos dados em uma variável

produtos = ['arroz', 'feijão', 'laranja', 'banana', 1, 2, 3, 4]
#              0         1         2          3
#item1, item2, item3, *outros = produtos  # Desempacotado

item1, item2, *outros, item8 = produtos

# item1 = produtos[0]
# item2 = produtos[1]
# item3 = produtos[2]
# item4 = produtos[3]

print(item1)
print(item2)
print(outros)
print(item8)
# print(item8)
