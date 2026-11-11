print("Vamos calcular seu IMC?")
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite sua altura (m): ").replace(",", "."))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida!")