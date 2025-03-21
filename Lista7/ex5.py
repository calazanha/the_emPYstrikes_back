catalogo = {
    101: ("Notebook", 3500.00),
    102: ("Smartphone", 2200.00),
    103: ("Fone de Ouvido", 150.00),
    104: ("Monitor", 800.00),
    105: ("Teclado", 120.00)
}

print("=== Catálogo de Produtos ===")
print("Códigos disponíveis:", ', '.join(map(str, catalogo.keys())))

codigo = int(input("\nDigite o código do produto que deseja consultar: "))

if codigo in catalogo:
    nome, preco = catalogo[codigo]
    print(f"\nProduto encontrado:")
    print(f"Nome: {nome}")
    print(f"Preço: R${preco:.2f}")
else:
    print("Código não encontrado no catálogo.")
