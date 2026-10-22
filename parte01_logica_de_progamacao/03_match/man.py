x =float(input("informe um numero: ").replace(",","."))
y = float(input("informe outro numero: ").replace(",","."))
print(f"('-'*20) Escolha uma operação: ('-'*20")
print(f"1 - Soma")
print(f"2 - Subtração")
print(f"3 - Multiplicação")
print(f"4 - Divisão")

operador = input("operação desejada: "). strip()

match operador:
    case "1":
        print(f"O resultado da soma é: {x + y}")
    case "2":
        print(f"O resultado da subtração é: {x - y}")
    case "3":
        print(f"O resultado da multiplicação é: {x * y}")
    case "4":
        print(f"O resultado da divisão é: {x / y}")
    case _:
        print("Operação inválida. Tente novamente.")