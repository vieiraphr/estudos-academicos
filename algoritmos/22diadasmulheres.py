print("Promoção especial - Dia da Mulher 💐")

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ").strip().upper()
valor = float(input("Digite o valor das compras: R$ "))

if sexo == "F":
    desconto = valor * 0.13
else:
    desconto = valor * 0.05

valor_final = valor - desconto

print(f"\nCliente: {nome}")
print(f"Valor original: R$ {valor:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")