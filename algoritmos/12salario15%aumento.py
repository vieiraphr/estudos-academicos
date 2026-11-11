import random

nome = input("Digite o nome do funcionário: ")
salario = random.randint(1500, 8000)
aumento = salario * 0.15
salario_final = salario + aumento
print(f"O funcionário {nome} recebia um salário de R${salario:.2f} antes de seu aumento.")
print(f"Pós aumento, o salário de {nome} ficou R${salario_final:.2f}.")