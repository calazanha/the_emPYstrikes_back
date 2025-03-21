tradutor = {
    "casa": "house",
    "livro": "book",
    "carro": "car",
    "gato": "cat",
    "cachorro": "dog",
    "escola": "school",
    "amor": "love",
    "comida": "food",
    "água": "water",
    "sol": "sun"
}

palavra_pt = input("Digite uma palavra em português para traduzir: ").strip().lower()

if palavra_pt in tradutor:
    traducao = tradutor[palavra_pt]
    print(f"A tradução de '{palavra_pt}' para o inglês é '{traducao}'.")
else:
    print(f"Tradução para '{palavra_pt}' não encontrada no dicionário.")
