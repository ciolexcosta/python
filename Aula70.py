# List Comprehension
# mais simples de se escrever
# utilizado quando você precisa criar uma nova lista a partir de uma existente
# [Expressão for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []

# for iten in frutas1:
#     if 'b' in iten:
#         frutas2.append(iten)
frutas2 = [iten for iten in frutas1 if 'b' in iten]

print(frutas2)
