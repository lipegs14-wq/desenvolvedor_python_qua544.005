try:
    nome = input("informe sua nome: "). strip(). title()
    idade = int(input("informe sua idade: "))

    print(f"nome do usuario: {nome}")
    print(f"idade do usuario: {idade} anos")
except Exception as e:
    print(f"nao foi possivel executar a acao: {e}.")
finally:
    print("fim do programa com sucesso")
    