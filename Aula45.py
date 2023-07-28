# Function (funções)
# - DRY - Dont repeat yourself
# - Vários argumentos(xargs) identificando o parametro
# Criar uma função que armazena números e Strings(dados)
# 2 asteriscos significa, vários argumentos + varios parametros

def agencia(**carro):  # ** vários argumentos e vários parametros
    return carro


# Definido na passagem da função
print(agencia(marca='gol', cor='Branca', motor=1.0, placa=1234))
print(agencia(marca='gol', cor='azul', motor=1.0))
print(agencia(marca='gol', cor='preto'))
