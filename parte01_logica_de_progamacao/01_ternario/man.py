nome = input("inforne seu nome: "). strip().title()
idade = int(input("informe sua idade: "))

print(f"{nome}! Você é {'maior' if idade >= 18 else 'menor'} de idade.")