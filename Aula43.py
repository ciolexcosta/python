# Functions (funções)
# - DRY = dont repeat yourself
# - Realizam uma tarefa
# - Calcula e retorna um valor

def cliente1(nome):  # tarefa, executa porém não guarda
    print(f'Olá {nome}')
#  cliente1('Maria')


def cliente2(nome):  # Executa algo e retorna, guarda o resultado, pode-se usar em variável
    return f'Olá {nome}'

#  cliente2('José')
#  print(cliente2('José'))


x = cliente1('Maria')  # apenas executa
y = cliente2('José')  # return


print(x)
print(y)
