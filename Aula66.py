# Lambda Function
# É uma função (pequena) sem nome
# Pode ter vários argumentos, mas somente 1 expressão
# Muito utilizado dentro de outras funções
# Código mais 'Clean'
# def somar(x):
#     return x + 10
# print(somar(2))

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4


print(somar(2))


