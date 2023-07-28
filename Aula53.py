# listas

cor_cliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('Cor em estoque')
else:
    print('Cor sem estoque')
