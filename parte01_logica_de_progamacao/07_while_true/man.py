#importar biblioteca
import os

#limpar a tela
os.system("cls"if os.name == "nt" else "clear")

#loop
while True:
    aluno = input("informe o nome do aluno: ").strip().title()
    try:
      nota = float(input("informe uma nota de 0 a 10: ").replace(",","."))
      if nota >= 0 and nota <= 10:
               if nota >= 7:
                   print(f"o aluno {aluno} foi aprovado.")
               elif nota >= 5:
                   print(f"o aluno {aluno} esta de recuperacao")
               else:
                   print(f"o aluno {aluno} foi reprovado.")
      else:
                print("nota invalida, tente novamente.")
    except Exception as e:
            print(f"nao foi possivel calcular a media: {e}.")
    continuar = input("deja inserir outra nota?'sim' para prosseguir. qualquer outro valor para encerrar: ").strip().lower()

    if continuar == "sim":
            os.system("cls"if os.name == "nt" else "clear")
            continue  
    else:
            break