print("Bem vindo ao PayDay Company.")

nome = input("Digite seu nome: ")
salario_atual = float(input("Seu salário atual: "))
tempo_empresa = int(input("Digite o tempo de empresa (anos): "))

if tempo_empresa == 3:
    aumento = 0.03
elif 4 <= tempo_empresa <= 9:
    aumento = 0.125
elif tempo_empresa >= 10:
    aumento = 0.20
else:
    aumento = 0

salario_final = salario_atual * (1 + aumento)

if aumento > 0:
    print(f"Você recebeu um aumento de {aumento*100:.2f}%!")
    print(f"Seu salário agora é R${salario_final:.2f}")
else:
    print("Muito cedo para aumentos...")