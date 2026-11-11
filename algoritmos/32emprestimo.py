valor_casa = input("Digite o valor da casa: R$").replace(".", "").replace(",", ".")
valor_casa = float(valor_casa)

salario_comprador = input("Qual é o seu salário atual? R$").replace(".", "").replace(",", ".")
salario_comprador = float(salario_comprador)

anos = int(input("Em quantos anos deseja pagar? "))

meses = anos * 12
prestacao = valor_casa / meses
limite_salario = salario_comprador * 0.30

print(f"\nPrestação mensal: R${prestacao:.2f}")
print(f"Limite permitido (30% do salário): R${limite_salario:.2f}")

if prestacao > limite_salario:
    print("O seu empréstimo não foi aprovado!")
else:
    print("Parabéns! O seu empréstimo foi aprovado :)")