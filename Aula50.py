# Listas
# Armanzenar mais de uma informação em variáveis
# Manter a sequencia dos dados em uma variável


numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']
final = numeros * 2
print(f' {final} lista multiplicada por 2')
final = numeros + letras
print(f'{final} lista numeros + letras')
numeros.extend(letras)
print(f'{numeros} lista numeros extend letras')

# sublistas           0                1
itens = [['item1', 'item2'], ['item3', 'item4']]
# itens     0          1         0        1

print(itens[0])
print(itens[1])
print(itens[0][0])
print(itens[0][1])
print(itens[1][0])
print(itens[1][1])



