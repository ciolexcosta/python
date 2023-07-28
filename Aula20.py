#  string com método
mensagem = 'eu adoro comida caseira'
#           0123456789
print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())
print(mensagem.find('c'))  # é case sensitive
print(mensagem.find('adoro'))
print(mensagem.replace('a', 'e'))
print(mensagem.replace('caseira', "feita em casa"))
mensagem2 = '     Eu adoro comida caseira'
print(mensagem2.strip())  # retira espaços na frente
