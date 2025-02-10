def resumo_sanduiche(*itens):
    print("\nResumo do sanduíche:")
    for item in itens:
        print(f"- {item}")

resumo_sanduiche('pão', 'queijo', 'presunto', 'alface', 'tomate')
resumo_sanduiche('pão', 'queijo', 'presunto')
resumo_sanduiche('pão', 'queijo', 'presunto', 'alface', 'tomate', 'maionese', 'ketchup')