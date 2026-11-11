print("Bem-vindo ao sistema de reajuste salarial!")

salario = float(input("Digite o salário atual do funcionário: R$").replace(",", "."))
genero = input("Digite o gênero do funcionário (M/F): ").strip().upper()
anos = int(input("Há quantos anos o funcionário trabalha na empresa? "))

novo_salario = salario  # Inicializa

if genero == "F":
    if anos < 15:
        aumento = 0.05
    elif anos <= 20:
        aumento = 0.12
    else:
        aumento = 0.23
elif genero == "M":
    if anos < 20:
        aumento = 0.03
    elif anos <= 30:
        aumento = 0.13
    else:
        aumento = 0.25
else:
    aumento = 0
    print("Gênero inválido! Sem reajuste aplicado.")

novo_salario = salario * (1 + aumento)
print(f"O novo salário do funcionário é: R${novo_salario:.2f}")