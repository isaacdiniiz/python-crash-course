from random import choice

lista = [10, 7, 4, 8, 18, 64, 37, 9, 30, 22, 'b', 't', 'f', 'g', 'e']
lista_sorteada = []

for _ in range(4):
    element = choice(lista)
    lista_sorteada.append(element)

print(f"Qualquer bilhete que corresponda a {lista_sorteada} ganha um premio!")