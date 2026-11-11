print("Bem vindo ao MoneyHealth!")
nome = input("Qual é o seu nome? ")
horas = int(input(f"Ok {nome}! Quantas horas de atividade física você realizou este mês? "))
if horas <= 10:
    pontos = 2 * horas
elif horas <= 20:
    pontos = 5 * horas
else:
    pontos = 10 * horas
print(f"Você tem {pontos} pontos!")
conversao = pontos * 0.05
print(f"Parabéns! Seu saldo final é: R${conversao:.2f}")




