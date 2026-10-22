nome = input("informe sua nome: "). strip(). title()
idade = int(input("informe sua idade: "))
altura = float(input("informe sua altura em metros"). replace(",","."))

if idade >= 12 and altura >= 1.35:
    print(f"{nome}! Você pode entrar no brinquedo.")
else:
    print(f"{nome}! Você não pode entrar no brinquedo.")