def abertura_segura_de_arquivo():
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")

abertura_segura_de_arquivo()
