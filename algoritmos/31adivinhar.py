import random

numero = random.randint(0, 10)
adivinhar = int(input("Digite um número:"))
diferenca = numero - adivinhar
print (f"O número sorteado foi {numero}")
if adivinhar == numero:
    print("Você acertou!")
else:
    print(f"Você errou por {diferenca}!")