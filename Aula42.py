# funções soma, parametro e argumento default
def boas_vindas(quantidade, nome='Linda'):  # non default, default
    print(f'Olá {nome}.')
    print(f'Temos {quantidade} laptops em estoque')

# default é aquele que você define o valor do parametro(nome)
# non default é aquele que vocÊ não define o valor do parametro nome='linda' sempre no final
# ordem = non default, default. Fora da ordem ou default 1º gera erro
# não pode haver 1º default e 2º non default


boas_vindas(10)
