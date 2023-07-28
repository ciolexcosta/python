# LISTAS 2
# Armazena mais de uma informação em variáveis
# Manter a sequencia dos dados em uma variável
cidade1 = 'Rio de janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Porto Velho', 'Goiania']
#                0                1             2            3
cidades.append('São Luis')  # adiciona elemento no final da lista
cidades.append('Rolim de Moura')

cidades[0] = 'Brasilia'  # troca de dado na lista, pelo index
cidades.remove('Porto Velho')  # remove o dado pelo nome
cidades.insert(2, 'Rio Preto')  # insere o dado no (index, dado)
cidades.pop(1)  # remove pelo index e retorna o removido
cidades.sort()  # organiza a lista em ordem alfabetica
print(cidades)
print(cidades[0])
