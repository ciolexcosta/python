# Function (funções)
# - DRY - Dont repeat yourself
# - Vários argumentos(xargs)
# Criar uma função que soma vários numeros
# Base do sistemas
def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


x = soma(2, 3, 4, 7)
print(x)