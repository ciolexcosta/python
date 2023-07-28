# Erros
# Excelente para testes
# Não realiza o 'Stop' no programa
# Mensagens customizadas quando encontra um erro
# else e finally
try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor inteiro')
finally:
    print('Executado de qualquer forma "finally" ')

# else:
#     print('Usuário digitou um valor correto!')
#     resultado = valor * 2
#     print(resultado)
print('Final do codigo - fora do try')

