nome = str(input("Nome do funcionário:"))
salario = float(input("Salário:").replace(",", "."))
print (f"O funcionário {nome} teve um salário de R${salario:.2f} em Junho")
