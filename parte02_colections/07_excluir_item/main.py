
frutas = [
    'maca',
    'pera',
    'manga',
    'morango',
    'melancia',
    'goiaba',
    'maracuja',
]

while True:
    for n, fruta in enumerate (frutas):
        print(f"indice {n}: {fruta}")

        print("1 - alterar fruta")
        print("2 - encerrar pograma")
        opcao = input("opcao desejada: "). strip()

        match opcao:
            case "1":
                indice = int(input("informe o indice a ser excluido: "))
                del(frutas[indice])
                print("fruta excluida com sucesso:")
                continue

            case "2": 
                print("opcao invalida.")
                break

            case _:
                print("opcao invalido.")
                continue