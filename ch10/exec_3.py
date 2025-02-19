from pathlib import Path

path = Path('guest.txt')

nome = input("Qual é o seu nome? ")
path.write_text(nome)