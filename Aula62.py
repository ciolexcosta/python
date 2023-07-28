# Dicionario
# utiliza index no formato de keys e values
# aceita String, integer, float, boolean

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'Aprovação': True}
print(aluno)
aluno['nome'] = 'José'
print(aluno['nome'])
aluno.update({'nome': 'Josefina', 'nota_final': 'B'})
print(aluno)
aluno.update({'endereco': 'Rua A'})
print(aluno)
print(aluno.get('endereco', 'Não existe'))  # se existir retorna endereco, contrario a msg
del aluno['idade']
print(aluno)

