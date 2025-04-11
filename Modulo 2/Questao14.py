import pickle
numeros = [1, 2, 3, 4, 5]
with open("dados.bin", "wb") as f:
    pickle.dump(numeros, f)

with open("dados.bin", "rb") as f:
    dados = pickle.load(f)
    print("Números lidos do binário:", dados)
