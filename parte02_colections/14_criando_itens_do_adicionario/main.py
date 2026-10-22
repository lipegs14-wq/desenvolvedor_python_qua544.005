import os


usuarios= []

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - cadastrar novo usuario")
    print("2 - exibir tabela de usuarios")
    print("3 - sair do programa")
    opcao = input("opcao desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
         usuario = []
         usuario('nome') = input("informe seu nome: "). strip(). title()
         usuario('idade') = int(input('informe a idade: '))
         usuario('email')=  input("nforme o email: ")
         usuario('cpf') = input('informe o cpf: ').strip(). lower()
         usuario.appemd(usuario)
         print(f"{usuario.get('nome')} cadastro concluido")
         continue
        case "2":
                 for usuario in usuarios:
                       for chave, valor in usuarios.item():
                            print(f"{chave.capitalize()}: {valor}")
                            print(f"('_' *40)")
                            continue
        case "3":
            break
        case _:
            print("opcao invalida.")
            continue