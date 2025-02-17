from random import choice

lista = [10, 7, 4, 8, 18, 64, 37, 9, 30, 22, 'b', 't', 'f', 'g', 'e']
lista_sorteada = []

for _ in range(4):
    element = choice(lista)
    lista_sorteada.append(element)

print(f"Qualquer bilhete que corresponda a {lista_sorteada} ganha um premio!")

count = 0
while True:
    my_ticket = []
    for _ in range(4):
        element = choice(lista)
        my_ticket.append(element)

    count += 1
    if my_ticket == lista_sorteada:
        break

print(f"O loop teve que ser executado {count} vezes para eu vencer!")