import os

nomes= ["alex","chaelotte","scarlet","john","michele","connor"]

os.system("cls")
while True:
 for a, nomes in enumerate(nomes):
    print("indice {n}: {nomes}")

    
 print("1 - alterar item da lista")
 print("2 - finalizar")
 opcao = input("opcao desejada"). strip()

 match opcao:
           case "1":
                indice = int(input("informe o indice a ser alterado:"))

                nomes[indice] = input("informe novo nome: "). strip(). title()
                os.sysstem("cls" if os.name == "nt" else "clear")
                print("item da lista alterado com sucesso")
                continue
           case 2:
        
            os.system("cls" if os.name == "nt" else "clear")
 for n, nome in enumerate(nomes):
                    print()