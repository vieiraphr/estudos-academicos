while True:
    nome = input("Bem vindo(a) ao RHSystem! Digite seu nome completo: ")
    print(f"Bem vindo(a), {nome}!")

    dias = int(input("Quantos dias você trabalhou no mês? "))

    if dias <= 0 or dias > 31:
        print("Essa resposta não pode ser validada, tente novamente.\n")
    else:
        break  # só sai quando for válido

horas_por_dia = 8
valor_hora = 25

salario = dias * horas_por_dia * valor_hora

print(f"{nome}, seu salário este mês é: R$ {salario:.2f}")


