import os


os.system("cls" if os.name == "nt" else "clear")

while True:

    print("1 - gravar novo arquivo")
    print("2 - abrir e ler o arquivo")
    print("3 - sair do pograma")
    opcao = input("opcao desejada: "). strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            novo_texto = input("digite o seu texto: ")
            novo_arquivo = input("informe nome do arquivo: "). strip()

            with open(f"15_gravando_arquivos/{novo_arquivo}.txt","w", encoding="utf-8") as f:
                f.write(novo_texto)
                continue
        case "2":
            abrir_arquivo = input("informe o nome do ,txt que deseja abrir:").strip()
            with open(f"15_gravando_arquivos/{novo_arquivo}.txt","w", encoding="utf-8") as f:
                texto = f.read()
                print(texto)
                continue
        case "3":
            print("programa finalizado")
            break
        case _:
            print("opcao invalida")