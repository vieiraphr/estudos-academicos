import random

print("Bem-vindo ao Jokenpô!")
print("Escolha sua opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

jogador = int(input("Digite o número da sua escolha: "))

opcoes = ["Pedra", "Papel", "Tesoura"]

computador = random.randint(1, 3)

print(f"Você escolheu: {opcoes[jogador-1]}")
print(f"O computador escolheu: {opcoes[computador-1]}")

if jogador == computador:
    print("Empate!")
elif (jogador == 1 and computador == 3) or \
     (jogador == 2 and computador == 1) or \
     (jogador == 3 and computador == 2):
    print("Você venceu! 🎉")
else:
    print("Você perdeu 😢")