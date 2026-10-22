nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg "). replace(",",".")) 
altura = float(input("Digite sua altura em metros "). replace(",","."))

imc = peso / (altura ** 2)
print(f"{nome}, seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com o peso normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")