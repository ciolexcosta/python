# Dicionario
# utiliza index no formato de keys e values
# aceita String, integer, float, boolean

aluno = {'nome': 'Ana',
         'idade': 16,
         'nota_final': 'A',
         'Aprovação': True,
         'Materias': ['Fisica', 'Matematica', 'Ingles']
         }

for keys, values in aluno.items():
    print(keys, values)

print(aluno.items())
print(aluno.keys())
print(aluno.values())


print(aluno.get('Materias'))
print(len(aluno))
