import os
os.system("cls")

nome = input("Digite o nome do aluno: "). strip(). title()
idade = int(input("Digite a idade do aluno: "))

os.system("cls") 


while True:
  
    sala = int(input("escolha uma sala de 1 a 5: "))

    if idadeuj == 0:
        print("Saindo da sala...")
        break
    elif sala == 1:
        filme_escolhido = {"nome": "Aventura no Espaço", "sala": 1, "classificacao": 10}
    elif sala == 2:
        filme_escolhido = {"nome": "Mistério na Floresta", "sala": 2, "classificacao": 12}
    elif sala == 3:
        filme_escolhido = {"nome": "Comédia Maluca", "sala": 3, "classificacao": 14}
    elif sala == 4:
        filme_escolhido = {"nome": "Ação Explosiva", "sala": 4, "classificacao": 16}
    elif sala == 5:
        filme_escolhido = {"nome": "Terror Assustador", "sala": 5, "classificacao": 18}

        if sala >= filme_escolhido["classificacao"]:
            print(f"\n===== INGRESSO =====")
            print(f"Nome: {nome}")
            print(f"Idade: {idade} anos")
            print(f"Filme: {filme_escolhido['nome']}")
            print(f"Sala: {filme_escolhido['sala']}")
            print(f"Classificação indicativa: {filme_escolhido['classificacao']} anos")
            print("====================")
            print("Ingresso emitido com sucesso!")
    
    sala_escolhida = int(input("\nDigite o número da sala desejada: "))
    
    if sala_escolhida == 0:
        print

    if idade >= filme_escolhido["classificacao"]:
        print("\n===== INGRESSO =====")
        print(f"Nome: {nome}")
        print(f"Idade: {idade} anos")
        print(f"Filme: {filme_escolhido['nome']}")
        print(f"Sala: {filme_escolhido['sala']}")
        print( f"Classificação indicativa: "
            f"{filme_escolhido['classificacao']} anos")
        print("====================")
        print("Ingresso emitido com sucesso!")
        break
    else:
        print("\nEntrada não permitida!")
        print( f"O filme exige idade mínima de "
         f"{filme_escolhido['classificacao']} anos.")
        print("Escolha outro filme.")