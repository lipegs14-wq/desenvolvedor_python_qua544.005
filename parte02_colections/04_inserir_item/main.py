import os

tarefa = []

os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela do terminal (Windows)

while True:

    print("1 - inserir ums nova tarefa")
    print("2 - finalizar lista")
    opcao = input("opcao desejada: "). strip() 
    match opcao:
        case "1":
         nome_tarefa = input("Digite a nova tarefa): ")
         tarefa.append(nome_tarefa)
         continue
        case "2":
         os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela do terminal (Windows)

         for n, tarefa in enumerate(tarefa, start=1):
            print(f"{n} - {tarefa}")
            break
        case _:
         print("opcao invalida")