# List Comprehension
# mais simples de se escrever
# utilizado quando você precisa criar uma nova lista a partir de uma existente
# [Expressão for iten in itens]

# valores =[]

# for x in range(6):
#     valores.append(x * 10)
# print(valores)

valores = [x * 10 for x in range(6)]
print(valores)
