import random

# Gera uma lista com 6 números aleatórios entre 1 e 60
numeros = random.sample(range(1, 61), 6)

# Formata a lista em uma string separada por "-"
dezenas = "-".join("{:02d}".format(num) for num in numeros)

# Imprime as dezenas geradas
print(dezenas)
