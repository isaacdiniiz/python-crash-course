from pathlib import Path

path = Path('guest_book.txt')
conteudo = ''

while True:
    convidado = input('Digite o nome do convidado (quit para fechar): ')
    if convidado == 'quit':
        break
    
    conteudo += convidado + '\n'

path.write_text(conteudo)