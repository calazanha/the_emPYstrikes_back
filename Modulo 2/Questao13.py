with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(f"Total de linhas: {len(linhas)}")
    for linha in linhas:
        print(linha.strip())
