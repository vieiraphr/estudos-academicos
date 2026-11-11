print("Bem vindo a área do aluno!")
nome = str(input("Digite seu nome:"))
nota_1 = float(input("Digite sua primeira nota:"))
nota_2 = float(input("Digite sua segunda nota:"))
media = (nota_1 + nota_2) / 2
print(f"Sua média foi {media:.2f}")
if media >= 7:
    print("Parabéns! Você está aprovado!")
else:
    print("Você está reprovado!")
