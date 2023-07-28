from sys import getsizeof
# Generator Expressions
# Uma forma mais rápida para criar listas, dicionários e etc
# Menos memória alocada
# valores em bytes

numeros = [x * 10 for x in range(1000000)]
print(type(numeros))
#print(numeros)
print(getsizeof(numeros))
print('==================')
numeros = (x * 10 for x in range(1000000))
print(type(numeros))
#print(list(numeros))
print(getsizeof(numeros))