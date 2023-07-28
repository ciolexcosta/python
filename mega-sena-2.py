import random

# Pedir ao usuário quantas sequências deseja gerar
n = int(input("Quantas sequências você deseja gerar? "))

# Loop para gerar as sequências
for i in range(n):
    # Gerar 6 números aleatórios entre 1 e 60 sem repetição
    dezenas = random.sample(range(1, 61), 6)

    # Ordenar as dezenas em ordem crescente
    dezenas.sort()

    # Imprimir as dezenas separadas por "-"
    print("-".join("{:02d}".format(d) for d in dezenas))
